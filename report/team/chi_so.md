# Chỉ số, event và rủi ro kinh tế · Nhiệm vụ E

## E1 · Chỉ số

| Loại | Chỉ số | Công thức | Chạy thử |
| --- | --- | --- | ---: |
| Chính | Đóng trong 24 giờ và không mở lại trong 7 ngày | Số yêu cầu thỏa cả hai điều kiện / tổng yêu cầu đã đủ thời gian theo dõi | 994/1.200 = 82,83% |
| Sử dụng | Tỉ lệ sửa hoặc bỏ gợi ý | Số quyết định sửa hoặc bỏ / số yêu cầu được xem lại | 48/177 = 27,12% |
| An toàn | Tỉ lệ mở lại trong 7 ngày | Số yêu cầu mở lại trong 7 ngày / tổng yêu cầu đủ thời gian theo dõi | 51/1.200 = 4,25% |
| Sử dụng bổ sung | Độ bao phủ gợi ý | Yêu cầu có gợi ý hiển thị / yêu cầu đủ điều kiện trong nhánh thử nghiệm | Đo trong pilot |
| An toàn bổ sung | Tỉ lệ yêu cầu hoàn trùng | Yêu cầu có hơn một giao dịch hoàn phí đã xác nhận / yêu cầu đã hoàn | Đo trong pilot |

Đây là số mô tả đợt chạy thử. Pilot có đối chứng cùng thời gian để ước lượng tác động của trợ lý.

## Event

Mọi event mang `request_id`, `trace_id` và thời điểm UTC. Với luồng thủ công, dịch vụ tiếp nhận tạo `trace_id` khi mở yêu cầu. Với luồng agent, giữ khóa nối các lượt chạy theo `request_id`.

| Event | Ai ghi | Thuộc tính bổ sung | Thời điểm |
| --- | --- | --- | --- |
| request_opened | Hệ thống yêu cầu | depot, staff_id, nhánh, loại, đủ điều kiện | Khi mở ca |
| agent_run_finished | Agent | run_id, attempt, token, tool_calls, status | Khi xong từng lượt |
| suggestion_shown | Giao diện CSKH | staff_id, suggestion_id | Khi hiển thị gợi ý |
| review_finished | Giao diện CSKH | giữ/sửa/bỏ, thời lượng | Khi nhân viên quyết định |
| rework_finished | Giao diện CSKH | lý do, thời lượng | Khi làm lại xong |
| request_closed | Hệ thống yêu cầu | thời điểm đóng | Khi đóng ca |
| request_reopened | Hệ thống yêu cầu | thời điểm mở lại, lý do | Khi mở lại |
| refund_confirmed | Dịch vụ thanh toán | transaction_id, số tiền | Khi xác nhận giao dịch |

Tính chỉ số chính và mở lại từ request_opened, request_closed, request_reopened. Tính sửa/bỏ từ review_finished; độ bao phủ từ request_opened và suggestion_shown. Tính hoàn trùng từ các transaction_id duy nhất của refund_confirmed theo request_id.

## E2 · Rủi ro kinh tế

| Rủi ro | Tác động | Dấu hiệu theo dõi | Hành động | Phụ trách |
| --- | --- | --- | --- | --- |
| Làm lại tăng | Gấp đôi làm CPS từ 4.472 đ lên 6.787 đ (+51,77%, simulated) | Phút làm lại/yêu cầu tăng gấp đôi so với tuần gốc | Rà mẫu ca làm lại, giữ nguyên bậc pilot | Quản lý sản phẩm |
| Xem lại kéo dài | Xem lại 100% cho 11.743–12.415 đ/việc thành công (simulated) | Vẫn xem lại toàn bộ cuối bậc 25% hoặc thời lượng trung bình vượt 4,8 phút/ca | Kiểm tra các nhóm ca có thể giảm tỷ lệ xem lại dựa trên số an toàn | Trưởng nhóm CSKH |
