# Bảng chi phí · Nhiệm vụ A và B

Nguồn tính: `src/lab13.py` chạy trên hai CSV. Các bảng ghi `simulated` dùng số phút giả lập.

## A1 · Ba phép thử với p = 0,8

| Phép thử | Kết quả |
| --- | ---: |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Kết quả | Nguồn / nhãn |
| --- | ---: | --- |
| Token | 245.585 đ | Trace |
| Tool | 84.000 đ | Trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 đ | Trace |
| Xem lại | 1.780.000 đ | simulated |
| Làm lại | 2.264.000 đ | simulated |
| Tổng chi phí | 4.373.585 đ | simulated |
| Số việc thành công | 978 | Kết quả yêu cầu |
| Chi phí mỗi việc thành công | 4.472 đ | simulated |
| Hóa đơn token và tool trên mỗi yêu cầu | 274,7 đ | Trace |

- Chi phí mỗi việc thành công gấp **16,3 lần** hóa đơn chia số yêu cầu. Làm lại chiếm **51,8%** tổng chi phí. Cả hai là `simulated`.
- Theo quy ước B3, chi phí cả hệ thống ở mức 3 lượt là (4.373.585 + 222 × 12.000) / 1.200 ≈ **5.865 đ/yêu cầu** (`simulated`).

## A3 · Theo loại yêu cầu

Hai cột chi phí và so sánh với baseline là `simulated`.

| Loại | Số yêu cầu | Thành công | Lượt/yêu cầu | Chi phí/việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,02% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,05% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,33% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,41% | 1,88 | 10.215 đ | 0,85× |

Quốc tế tốn **22.515 đ** (`simulated`); tỉ lệ OK ở các lượt 1, 2, 3 lần lượt là **30%, 11,4%, 2,2%**. Lợi ích của các lượt bổ sung thấp trên tập yêu cầu phải chạy lại. Đối tác có tỉ lệ thành công **54,41%** và điều khoản riêng, nên pilot ưu tiên nội địa và hàng nặng.

## A4 · Chi phí cố định cho nội địa và hàng nặng

Giả định tổng lưu lượng giữ cơ cấu mẫu, với 900 việc thành công trong phạm vi trên 1.200 yêu cầu toàn hệ thống.

| Tổng yêu cầu/tháng | Việc thành công trong phạm vi/tháng | Cố định/việc | Chi phí/việc gồm cố định (`simulated`) | So với baseline (`simulated`) |
| --- | ---: | ---: | ---: | ---: |
| 45.000 | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| 22.500 | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

Cả hai mức đều thấp hơn 12.000 đ. Theo cách tính này, hòa vốn ở khoảng **6.212 yêu cầu toàn hệ thống/tháng** (`simulated`).

## B1 · Đổi từng yếu tố

Mọi chi phí và mức thay đổi trong bảng là `simulated`.

| Kịch bản | Chi phí/việc thành công | Thay đổi |
| --- | ---: | ---: |
| Giá token gấp đôi | 4.723,08 đ | +5,62% |
| Giá token giảm một nửa | 4.346,41 đ | −2,81% |
| Tỉ lệ xem lại gấp đôi | 6.292,01 đ | +40,70% |
| Tỉ lệ xem lại giảm một nửa | 3.561,95 đ | −20,35% |
| Số ca làm lại gấp đôi | 6.786,90 đ | +51,77% |
| Số ca làm lại giảm một nửa | 3.314,50 đ | −25,88% |
| Lương tăng 25% | 5.505,71 đ | +23,12% |
| Tối đa 2 lượt | 4.237,29 đ | −5,25% |
| Tối đa 1 lượt | 4.110,99 đ | −8,07% |

## B2 · Đổi một cặp và xếp hạng

- Token và xem lại cùng gấp đôi đưa chi phí lên **6.543,12 đ**, tăng **46,31%** (`simulated`).
- Ba yếu tố nhạy nhất là **làm lại (+51,77%)**, **xem lại (+40,70%)** và **lương (+23,12%)** (`simulated`).

## B3 · Giới hạn chạy lại

Chi phí hệ thống bằng tổng chi phí trợ lý cộng 12.000 đ cho mỗi ca không thành công theo quy ước bài. Các cột tiền là `simulated`.

| Giới hạn | Chi phí trợ lý | Ca không thành công | Chi phí hệ thống | Chi phí/việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

**2 lượt** có chi phí hệ thống thấp nhất (**6.901.220 đ**, `simulated`). Mức **1 lượt** có chi phí/việc thành công thấp nhất nhưng phát sinh thêm **85 ca** không thành công so với 2 lượt.

## B4 · Xem lại toàn bộ

Với 948 ca có lượt OK và 48 ca làm lại, xem lại 5 phút/ca cho chi phí **11.743 đ/việc** nếu làm lại 9 phút và **12.415 đ/việc** nếu dùng 15,3 phút từ dữ liệu (`simulated`). Ngưỡng hòa vốn tương ứng là **5,12** và **4,80 phút** xem lại mỗi ca. Pilot cần đo thời lượng xem lại và điều kiện giảm độ bao phủ mà vẫn an toàn.
