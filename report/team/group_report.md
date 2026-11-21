# Báo cáo nhóm · Lab 13

## 1. Thông tin

Lớp L3A · Nguyễn Vũ Hoàng (2A202603491) · Xem [TEAM.md](../../TEAM.md) về hình thức làm bài cá nhân.

## 2. Mục tiêu và cách tiếp cận

Đánh giá kinh tế trợ lý hoàn phí từ hai CSV, phân tích rủi ro và thiết kế pilot có đối chứng.

## 3. Giải pháp

- [A–B · Bảng chi phí](bang_chi_phi.md) tính trên trace và phân tích theo loại yêu cầu, giới hạn lượt chạy và khối lượng xem lại.
- [C · Bảng lỗi](bang_loi.md) có 20 nhãn cá nhân, 20 nhãn AI đối chiếu, mức trùng 20/20 và 5 phương án khắc phục.
- [D · Kế hoạch pilot](pilot_plan.yaml) chia ngẫu nhiên theo nhân viên, đối chứng cùng thời gian.
- [E · Chỉ số](chi_so.md) và [hồ sơ launch](ho_so_launch_v0.md) ghi bằng chứng, ngưỡng an toàn và rủi ro kinh tế.

## 4. Kết quả

Ba phép thử A1 đạt. Chi phí gốc là 4.472 đ/việc thành công (simulated). Đề xuất Go có điều kiện cho pilot nội địa và hàng nặng, với 20 nhân viên mỗi nhánh. [Phiếu rà soát Gate 2a](phieu_cham.md) ghi điểm thử bằng AI là 25/30.

## 5. Khó khăn và đóng góp

Bài được thực hiện cá nhân trong tình huống nêu ở TEAM.md. Phân công, bằng chứng và công cụ AI ghi trong báo cáo cá nhân.

## 6. Hạn chế và nguồn

Đợt chạy thử thiếu đối chứng. Chi phí phụ thuộc vào phút xem lại và làm lại giả lập. Thiết kế theo nhân viên chấp nhận mục tiêu 6 điểm phần trăm. Nguồn gồm hai CSV của đề và [công thức của lab](../../docs/du_lieu_va_cong_thuc.md).
