import io

#carpentry workshop daily log: day, chairs made, timber used(metres)
workshop_log = """Monday,8,24,3,2.0
Tuesday,6,18,2.5,1.3
Wednesday,10,18,3,2.2
Thursday,7,21,2,2.5
Friday,9,27,3.1,3.0
Saturday, 6,19,4,2.7
"""

total_chairs = 0
total_timber = 0
days = 0 
total_nails =0
total_paint = 0

f = io.StringIO(workshop_log)
for line in f:
    line = line.strip()
    if line:
        day,chairs,timber,nails,paint = line.split(",")
        chairs = int(chairs)
        timber = float(timber)
        nails  = float(nails)
        paint = float(paint)
        print(f"{day}: {chairs} chairs | {timber}m timber | {nails}kg nails")  
        total_chairs +=chairs
        total_timber +=timber
        total_nails +=nails
        total_paint +=paint
        days += 1
        print()
        print(f"\nTotal chairs made:{total_chairs}")
    
        print(f"Total timber used:{total_timber}m")
        print(f"Total nails used:{total_nails}kg")
    
        print(f"Total paint used:{total_paint}L")
        print(f"Average chairs per day:{total_chairs //days}")
        print(f"Average nails per day:{total_nails //days}kg")
