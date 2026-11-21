# Báo cáo cá nhân — Nguyễn Vũ Hoàng

- MSSV: 2A202603491
- Email: bacphan204@gmail.com
- GitHub: bacphan204-tech

## Phần việc phụ trách

Em làm Lab 13 cá nhân, kiêm viết code, kiểm số, gắn nhãn và đối chiếu ca lỗi, đồng thời giữ hồ sơ.

## Đóng góp và bằng chứng

- Mô hình chi phí, phân tích độ nhạy và tính cỡ mẫu trong [lab13.py](../../src/lab13.py).
- Kết quả chạy trên hai CSV gốc và ba phép thử A1 (1,20 · 1,25 · 1,25) trong [bảng chi phí](bang_chi_phi.md).
- [Bảng lỗi](bang_loi.md) ghi 20 nhãn em tự chọn, 20 nhãn AI đối chiếu và 5 phương án khắc phục. Em dùng AI để định dạng bộ nhãn của mình thành tệp.
- Hồ sơ quyết định và các căn cứ trong [hồ sơ launch v0](ho_so_launch_v0.md).

## Công cụ AI

Em dùng Codex để hỗ trợ triển khai Python và soạn tài liệu, ChatGPT để định dạng và đối chiếu nhãn. Kết quả được kiểm tra bằng hai CSV gốc, ba phép thử A1 và script kiểm tra phần C.

## Tự đánh giá

Phân tích cho thấy chi phí làm lại và xem lại ảnh hưởng nhiều hơn giá token. Khi tính cả chi phí nhân viên xử lý ca thất bại, giới hạn hai lượt cho tổng chi phí thấp nhất trong ba kịch bản được thử. Thiết kế pilot theo nhân viên giảm nguy cơ lan truyền giữa hai nhánh nhưng cần 299 ca đủ điều kiện trên mỗi người để hướng tới mức chênh 6 điểm phần trăm.
