import tempfile
import unittest
from pathlib import Path

from sort_documents import sort_folder


class DocumentSorterTests(unittest.TestCase):
    def test_sorts_mixed_files_and_logs_every_move(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            filenames = [
                "agreement.docx", "old_contract.doc", "photo.jpg",
                "evidence.jpeg", "diagram.png", "court_filing.pdf",
                "notice.txt", "client_email.eml", "spreadsheet.xlsx",
                "archive.zip", "UPPERCASE.PDF",
            ]
            for name in filenames:
                (folder / name).write_text("dummy content", encoding="utf-8")

            moved = sort_folder(folder)

            self.assertEqual(moved, len(filenames))
            self.assertTrue((folder / "Contracts" / "agreement.docx").exists())
            self.assertTrue((folder / "Contracts" / "old_contract.doc").exists())
            self.assertTrue((folder / "Evidence" / "photo.jpg").exists())
            self.assertTrue((folder / "Evidence" / "evidence.jpeg").exists())
            self.assertTrue((folder / "Evidence" / "diagram.png").exists())
            self.assertTrue((folder / "Filings" / "court_filing.pdf").exists())
            self.assertTrue((folder / "Filings" / "UPPERCASE.PDF").exists())
            self.assertTrue((folder / "Correspondence" / "notice.txt").exists())
            self.assertTrue((folder / "Correspondence" / "client_email.eml").exists())
            self.assertTrue((folder / "Other" / "spreadsheet.xlsx").exists())
            self.assertTrue((folder / "Other" / "archive.zip").exists())

            log_lines = (folder / "sort_log.txt").read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(log_lines), len(filenames))
            self.assertTrue(all("FROM:" in line and "TO:" in line for line in log_lines))

    def test_does_not_overwrite_same_named_file(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            (folder / "Contracts").mkdir()
            (folder / "Contracts" / "agreement.docx").write_text("existing", encoding="utf-8")
            (folder / "agreement.docx").write_text("new", encoding="utf-8")

            sort_folder(folder)

            self.assertEqual(
                (folder / "Contracts" / "agreement.docx").read_text(encoding="utf-8"),
                "existing",
            )
            self.assertEqual(
                (folder / "Contracts" / "agreement_1.docx").read_text(encoding="utf-8"),
                "new",
            )


if __name__ == "__main__":
    unittest.main()
