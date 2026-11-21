# Bảng lỗi và cách khắc phục · Nhiệm vụ C

**Người phụ trách:** Nguyễn Vũ Hoàng · **MSSV:** 2A202603491
**A:** Nguyễn Vũ Hoàng · **B:** ChatGPT (AI)
**Ngày lập bảng:** 21/11/2026

**Phương pháp:** Theo xác nhận của Nguyễn Vũ Hoàng, Hoàng tự chọn 20 nhãn A và dùng AI để định dạng thành tệp. ChatGPT chuẩn bị bộ B có đối chiếu đáp án tham khảo.

## Định nghĩa 5 loại theo nguyên nhân gốc

| Loại | Cách nhận diện |
| --- | --- |
| Do người dùng | Người dùng nhập/chọn sai. |
| Hệ thống | Trợ lý làm trái thiết kế/chính sách và lỗi đã lộ. |
| Ngữ cảnh | Kết quả đúng theo thiết kế nhưng cách áp dụng/diễn giải không phù hợp hoàn cảnh. |
| Giới hạn hệ thống | Thiếu dữ liệu, ngoài phạm vi hoặc không thể xử lý đáng tin cậy. |
| Ngầm | Có sai lệch không được nhận ra cho tới khi kiểm tra mẫu/kiểm toán. |

## Bảng gắn nhãn và đối chiếu

| Ca | A — Nguyễn Vũ Hoàng | B — ChatGPT (AI) | Trùng nhau? | Nhãn thống nhất | Nhãn tham khảo |
| --: | --- | --- | :---: | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống | Hệ thống |

**Đã điền:** A 20/20, B 20/20, nhãn thống nhất 20/20. **Đối chiếu A–B:** 20/20 (100%). **Đối chiếu nhãn tham khảo:** 20/20. Độ độc lập của hai lượt gắn nhãn chưa được chứng minh.

## Ghi chú phân loại 20 ca

| Ca | Nhãn đề xuất | Cơ sở đối chiếu / quy tắc phân biệt |
| --: | --- | --- |
| 1 | Do người dùng | Sai lệch xuất phát từ thao tác hoặc thông tin đầu vào; cần đọc lại nguyên văn ca. |
| 2 | Hệ thống | Đáp án tham khảo quy nguyên nhân cho hành vi hệ thống trái thiết kế. |
| 3 | Ngữ cảnh | Đáp án tham khảo chỉ ra bất cập của giả định/ngữ cảnh sử dụng. |
| 4 | Giới hạn hệ thống | Nguồn dữ liệu hoặc khả năng xử lý thiếu; chuyển giao đúng phạm vi. |
| 5 | Ngầm | Lỗi khó quan sát ngay, được phát hiện khi kiểm tra. |
| 6 | Do người dùng | Khách chọn sai mục; hệ thống có thể hỗ trợ phát hiện nhưng không đổi nguyên nhân gốc. |
| 7 | Hệ thống | Thông báo hoàn tiền không đi cùng xác nhận sổ cái; lỗi hệ thống đã lộ. |
| 8 | Hệ thống | Sai trích dẫn có thể nhìn thấy; không phải lỗi ngầm. |
| 9 | Do người dùng | Khách nhập mã sàn TMĐT thay cho mã vận đơn; cần kiểm tra đầu vào. |
| 10 | Ngữ cảnh | Đáp án tham khảo cho thấy giả định về hoàn cảnh khách không khớp. |
| 11 | Giới hạn hệ thống | Đáp án tham khảo phân loại thiếu dữ liệu hoặc ngoài khả năng xử lý. |
| 12 | Ngầm | Chi phí gấp 3 lần trong 3 tuần nhưng không ai nhận ra; lỗi hiệu quả bị ẩn. |
| 13 | Giới hạn hệ thống | Yêu cầu ngoài phạm vi; cách xử lý chưa tốt không đổi loại gốc. |
| 14 | Do người dùng | Đáp án tham khảo quy lỗi cho đầu vào/hành động của người dùng. |
| 15 | Hệ thống | Sai sót đã được nhân viên phát hiện; không phải lỗi ngầm. |
| 16 | Ngữ cảnh | Đáp án tham khảo phân loại giả định/ngữ cảnh không phù hợp. |
| 17 | Ngầm | Sai giá do cache/bảng giá cũ; chỉ thấy qua kiểm toán mẫu. |
| 18 | Ngữ cảnh | Số tiền đúng chính sách nhưng khách không hiểu cách tính. |
| 19 | Giới hạn hệ thống | Đáp án tham khảo xác định giới hạn về phạm vi/dữ liệu. |
| 20 | Hệ thống | Đáp án tham khảo cho thấy trợ lý sai chính sách/thiết kế. |

## Quy tắc phân biệt

- **Ca 6, 9:** Sai do khách chọn/nhập sai, không chuyển thành lỗi hệ thống chỉ vì giao diện cần cải thiện.
- **Ca 8, 15:** Hệ thống vì lỗi được phát hiện qua trích dẫn/nhân viên; “ngầm” chỉ dùng khi chưa được phát hiện.
- **Ca 12:** Ngầm vì chi phí tăng 3 lần suốt 3 tuần mà không ai thấy.
- **Ca 13:** Giới hạn hệ thống vì yêu cầu nằm ngoài phạm vi hỗ trợ.
- **Ca 18:** Ngữ cảnh vì số tiền đúng nhưng giả định khách hiểu công thức không phù hợp.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Các ngưỡng dưới đây là **ngưỡng giám sát đề xuất cho pilot**, không phải tỉ lệ đã đo từ trace.
Event cần chứa `trace_id`, `request_id` và thời điểm để đối soát.

| Ca | Loại lỗi | Phát hiện bằng gì (có ngưỡng/tần suất) | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`, theo dõi hằng ngày; rà nếu **>2%** yêu cầu/ngày nhập sai định dạng hoặc dùng mã sàn TMĐT thay mã vận đơn. | Nhận diện hai loại mã; kiểm tra và gợi ý chuyển sang mã vận đơn; không xác minh được thì hướng dẫn nhập lại, không tự đoán mã. | PM trợ lý hoàn phí |
| 7 | Hệ thống | Mỗi giờ đối soát event `refund_confirmed_to_customer` với `ledger_refund_ok` cùng `trace_id`; ngưỡng **0 ca** báo đã hoàn mà sổ cái chưa xác nhận. | Chỉ gửi “đã hoàn” sau xác nhận `ledger=ok`; nếu tool lỗi 503 sau tối đa 3 lần thì giữ trạng thái “đang xử lý”, chuyển nhân viên và không xác nhận hoàn tiền. | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Theo tuần đo event `request_reopened` có lý do `amount_not_understood` trong các ca số tiền đối soát đúng; rà nếu **>2%** ca giải thích tiền. | Hiện rõ công thức và thành phần hoàn tiền, ví dụ 30.000 đ × 50% = 15.000 đ; giải thích từng bước và cho phép hỏi lại trước khi đóng ca. | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason=thieu_du_lieu` hoặc `out_of_scope`; thống kê theo loại yêu cầu hằng ngày; rà nếu **>5%** trong phạm vi pilot. | Chuyển nhân viên kèm tóm tắt, dữ liệu thiếu và bước đã thử; không suy đoán. Tạm loại `quoc_te` khỏi phạm vi pilot theo A3. | PM trợ lý hoàn phí |
| 17 | Ngầm | Kế toán kiểm toán ngẫu nhiên **100 đơn/tuần** so với bảng giá hiện hành; cảnh báo từ **1 đơn sai** trong mẫu (≥1%). | Xóa cache khi bảng giá đổi; bắt buộc ghi `price_table_version`/`effective_date` vào trace; dừng dùng phiên bản cũ và rà lại đơn bị ảnh hưởng. | Kế toán trưởng |

## Kết luận CP3

Nhãn cá nhân và nhãn ChatGPT trùng **20/20**. Năm phương án khắc phục bao phủ đủ năm loại lỗi. Đối chiếu này dùng bộ B từ ChatGPT và chưa đủ điều kiện hai người gắn nhãn độc lập.
