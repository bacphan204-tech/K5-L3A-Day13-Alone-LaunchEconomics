"""Kiểm tra tính đầy đủ phần C; không xác nhận tính độc lập của hai người.

Chạy tại thư mục gốc repo:
  py kiem_tra_C.py
  py kiem_tra_C.py --require-complete
  py kiem_tra_C.py --require-human       # kiểm tra cột A đã đủ nhãn
  py kiem_tra_C.py --require-independent # mã 2: không có 2 người độc lập
"""
from pathlib import Path
from collections import Counter
import re, sys

src=Path('report/team/bang_loi.md')
if not src.is_file():
    sys.exit('FAIL: Không thấy report/team/bang_loi.md. Hãy chạy từ thư mục gốc repo.')
txt=src.read_text(encoding='utf-8')

def get_rows(begin,end):
    chunk=txt.split(begin,1)[1].split(end,1)[0]
    return [[v.strip() for v in line.strip().strip('|').split('|')]
        for line in chunk.splitlines() if re.match(r'^\|\s*\d+\s*\|',line)]
try:
    cases=get_rows('## Bảng gắn nhãn và đối chiếu','## Ghi chú phân loại 20 ca')
    notes=get_rows('## Ghi chú phân loại 20 ca','## Quy tắc phân biệt')
    fixes=get_rows('## Bảng khắc phục cho 5 ca','## Kết luận CP3')
except IndexError:
    sys.exit('FAIL: Không tìm thấy các đề mục bắt buộc.')
ref={'Do người dùng':[1,6,9,14], 'Hệ thống':[2,7,8,15,20], 'Ngữ cảnh':[3,10,16,18], 'Giới hạn hệ thống':[4,11,13,19], 'Ngầm':[5,12,17]}
by_case={v:k for k,ns in ref.items() for v in ns}
valid=set(ref)
if len(cases)!=20 or [int(r[0]) for r in cases]!=list(range(1,21)) or any(len(r)!=6 for r in cases):
    sys.exit('FAIL: Bảng nhãn thiếu ca hoặc cột.')
if any(r[1] not in valid or r[2] not in valid or r[4] not in valid or r[5]!=by_case[int(r[0])] for r in cases):
    sys.exit('FAIL: Thiếu nhãn A/B/nhãn chốt hoặc tham khảo sai.')
if len(notes)!=20 or [int(r[0]) for r in notes]!=list(range(1,21)):
    sys.exit('FAIL: Thiếu 20 ghi chú.')
if len(fixes)!=5 or {r[1] for r in fixes}!=valid or any(len(r)!=5 or not re.search(r'\d',r[2]) or not r[3] or not r[4] for r in fixes):
    sys.exit('FAIL: Thiếu bảng khắc phục 5 loại có ngưỡng và người phụ trách.')
matched=sum(r[1]==r[2] for r in cases)
correct=sum(r[4]==by_case[int(r[0])] for r in cases)
print('PASS: A 20/20, B 20/20, nhãn chốt 20/20, ghi chú 20/20, khắc phục 5/5.')
print('Phân bố nhãn chốt:',dict(Counter(r[4] for r in cases)))
print(f'Đối chiếu hình thức A/B: {matched}/20 = {matched*5}% (KHÔNG độc lập).')
print(f'Nhãn chốt trùng tham khảo: {correct}/20 (không phải đánh giá mù).')
print('Nguồn nhãn ghi trong báo cáo: A do Hoàng tự chọn theo xác nhận của Hoàng; B do ChatGPT đối chiếu.')
if '--require-independent' in sys.argv:
    print('PENDING: Rubric yêu cầu hai người gắn nhãn độc lập.')
    sys.exit(2)
