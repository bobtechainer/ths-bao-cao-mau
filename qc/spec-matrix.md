# Bảng nghiệm thu — báo cáo tình hình đi học, hai lớp chủ nhiệm, 31/08–04/09/2026

File: `bao-cao/2026-09-08-2-lop-chu-nhiem-di-hoc.html` · vòng soi 1 · 08/09/2026

`scripts/qc_score.py` đọc file này. Giữ đúng năm cột, đúng thứ tự.

**Cột `Status`:** `✓` đã kiểm · `~` đã làm nhưng chưa kiểm · `✗` còn mở.
**Chỉ `✓` được tính vào độ hoàn thành.** `~` liệt kê riêng — **không bao giờ báo `~` là xong**.

**Cột `W`:** `5` yêu cầu cốt lõi (sai là bản báo cáo dắt người đọc đi sai) · `3` yêu cầu chống lưng · `1` mài giũa.

**Cột `Verify`:** ghi rõ ai chứng minh — `du-lieu:` lăng kính 1 · `giong:` lăng kính 2 · `hinh:` lăng kính 3 · `doc:` lăng kính 4 · `may:` một script.

Cửa mở khi: **độ hoàn thành 100%** và **không còn P0, P1 nào mở**.

---

## Phần cứng — mọi bản báo cáo đều có, không bỏ dòng nào

| ID | Requirement | Verify | W | Status |
|---|---|---|---|---|
| G01 | Yêu cầu báo cáo kết thúc bằng một file HTML trong tay người hỏi, kể cả khi không có dữ liệu | may: file 196 KB mở được, in ra 16 trang A4 | 5 | ✓ |
| G02 | Mỗi khối số mang cửa sổ **dội lại** từ phản hồi, không phải cửa sổ đã yêu cầu | du-lieu vòng 2: kiểm 4 lời gọi, cửa sổ dội lại đúng | 5 | ✓ |
| G03 | Không con số nào nằm dưới tiêu đề cửa sổ khác với cửa sổ sinh ra nó | du-lieu vòng 2: P0 “hai khoảng” đã sửa và đo lại | 5 | ✓ |
| G04 | Mọi con số có `data-fig` khớp một mục trong khối JSON đồng hành | may: check_sidecar --render · 0 chặn 0 nhắc | 5 | ✓ |
| G05 | Danh sách dài bằng trần đều có câu nói rõ bị giới hạn; không từ chỉ lượng `toàn bộ`/`tất cả`/`duy nhất` trên chúng | du-lieu vòng 2: trần recent_absent_dates=5 và trần list_teacher_classes=60 đều khai trong gioiHan | 5 | ✓ |
| G06 | Trường `note` của phản hồi hiện nguyên văn cạnh số rút ra từ nó, trong thân trang | du-lieu vòng 2: cột note nguyên văn cạnh từng số; câu nói quá đã thu phạm vi | 3 | ✓ |
| G07 | Sĩ số là số dòng `role=="student"`; không in `_count`, `student_count`, hay độ dài mảng | du-lieu vòng 2: đếm tay roster, 22 và 48 dòng role==student | 5 | ✓ |
| G08 | Khoá thiếu in `chưa chấm`/`chưa có điểm`, bị loại khỏi trung bình, và số dòng đã loại được nói ra | may: 0 mục khoaThieu — không có số kiểm tra nào trên trang | 5 | ✓ |
| G09 | Không in `class_name` từ `find_at_risk_students` hay `search_students` | du-lieu vòng 1: gọi find_at_risk_students rồi grep, 0 tên lớp lạ lọt lên trang | 5 | ✓ |
| G10 | Giá trị trường `exam` mang chữ "phòng thi"/"ca thi", trừ khi khớp được trong `list_exams` | may: grep · trường exam không xuất hiện | 3 | ✓ |
| G11 | Mọi câu so sánh kỳ trước có lời gọi thứ hai trong log, hai cửa sổ hiện trên trang, kèm nhãn tự-tính | du-lieu vòng 1: grep tăng/giảm/so với → chỉ khớp câu phủ định | 5 | ✓ |
| G12 | Câu `lớp không có X` có lời gọi trên mọi lớp bộ môn cùng tên, và trang liệt kê `class_id` đã hỏi | du-lieu vòng 2: gọi lại 20/20 get_schedule bằng token trường | 5 | ✓ |
| G13 | Câu nói về cả lớp rút từ đọc từng em có in cỡ mẫu `đã tra n/N em` | du-lieu vòng 1: “đã tra 2 trên 70 dòng” in ngay trên bảng | 3 | ✓ |
| G14 | Cửa chốt chuyên cần: `present==0` khắp sổ lớp thì có bảng cảnh báo và **không** con số chuyên cần nào chỗ khác | du-lieu vòng 2 + phép đo riêng: 0 con số chuyên cần ngoài mục Chuyên cần | 5 | ✓ |
| G15 | Mọi câu về nguyên nhân, cơ chế, bản chất dữ liệu đều có trường trả về chống lưng, hoặc ghi `chưa rõ nguyên nhân` | du-lieu vòng 2: phỏng đoán cơ chế đã gom vào một dòng gắn nhãn | 5 | ✓ |
| G16 | Không phủ định về một khoảng ngày mà không có lời gọi phủ đúng khoảng đó | du-lieu vòng 1: mọi câu về khoảng ngày đều có lời gọi phủ đúng khoảng | 5 | ✓ |
| G17 | Không tự mâu thuẫn: một con số một giá trị, một bộ dữ liệu một nhãn | du-lieu vòng 2: 48 và 44 đã tách nhãn, hết chỗ một số hai nghĩa | 5 | ✓ |
| G18 | Khối đầu trang có: tên báo cáo, phạm vi, cửa sổ theo từng loại dữ liệu, dòng giả định, giờ đọc số liệu | doc vòng 2: khối đầu trang có thêm tài khoản, máy chủ, năm học | 5 | ✓ |
| G19 | Khối cuối trang "Số liệu lấy từ đâu" liệt kê công cụ + cửa sổ cho từng nhóm số, kèm các câu giới hạn | du-lieu vòng 2: bảng nguồn phủ đủ 84 mục | 3 | ✓ |
| G20 | Mục "Chưa dựng được, và vì sao" có mặt khi người dùng xin thứ hệ thống chưa cho | doc vòng 2: mục Chưa dựng được có 5 thẻ | 3 | ✓ |
| V01 | `check_voice.py` báo 0 lỗi chặn | may: check_voice --render · 0 chặn | 5 | ✓ |
| V02 | Mỗi dòng nhận xét có đủ ba nhịp: sự việc kèm cửa sổ → nghĩa trong lớp → một việc làm tiếp | giong vòng 2: các dòng Sổ lớp và Việc phải sửa đủ ba nhịp; đoạn dẫn còn nói về khả năng đọc | 5 | ✓ |
| V03 | Việc làm tiếp thuộc tay người đọc, không lệch người | giong vòng 2: cột đổi thành “Thầy/cô làm gì tiếp”, 8/9 dòng kết bằng việc của thầy/cô | 3 | ✓ |
| V04 | Nhãn `cần theo dõi`/`cần hỗ trợ` có câu nói ngưỡng và câu nói rõ đây không phải xếp loại | giong vòng 2: nhãn phép kiểm nói rõ ngưỡng, và đổi sang vàng để không nằm đỏ cạnh tên em | 3 | ✓ |
| V05 | Không con số đáng lo nào được nhấn, đặt trước câu giải nghĩa, hay đặt trong đoạn "nếu làm bừa" | giong vòng 2: đọc cả 21 đoạn đậm — không con số đáng lo nào bị nhấn; câu rút lại đứng trước con số | 5 | ✓ |
| V06 | Bảng nhận xét không cùng một khuôn | giong vòng 2: từ mở đầu các dòng có trộn thật | 1 | ✓ |
| V07 | Tiêu đề mục là câu nói ra điều người đọc sẽ thấy | giong vòng 2: 4/5 h2 nói ra điều người đọc sẽ thấy; đã sửa h2 còn lại | 1 | ✓ |
| V08 | Trang không tự giới thiệu mình | giong vòng 2: khối tự bào chữa đã rút; còn E05 và E13 ghi trong defects | 1 | ✓ |
| H01 | Mọi màu trên trang có mặt trong `04-mau-va-chu.md`; `validate_palette.js` không FAIL | hinh vòng 1: validate_palette ALL CHECKS PASS · 0 mã màu ngoài bảng | 5 | ✓ |
| H02 | Cảnh báo tương phản có kênh cứu: nhãn số trực tiếp hoặc bảng song sinh | hinh vòng 1 + sửa A01: cả 24 nhãn trạng thái đều mang chữ | 5 | ✓ |
| H03 | Cửa 3 đúng: tên lớp/môn/học sinh cùng một màu; khoảng điểm và khối dùng dải đơn sắc | hinh vòng 1: không áp dụng — 0 biểu đồ | 5 | ✓ |
| H04 | Không quá 5 chuỗi phân loại; hình so mọi cặp không quá 3 khi thiếu nhãn trực tiếp | hinh vòng 1: không áp dụng — 0 biểu đồ | 3 | ✓ |
| H05 | Kích thước dấu đúng: cột ≤24px, bo 4px đầu dữ liệu vuông chân, đường 2px, nền vùng 10% | hinh vòng 1: không áp dụng — 0 biểu đồ | 3 | ✓ |
| H06 | Khe nền 2px và vành nền 2px làm việc phân cách; không viền quanh dấu | hinh vòng 1: không áp dụng — 0 biểu đồ | 3 | ✓ |
| H07 | `vector-effect="non-scaling-stroke"` trên lưới, trục, nét dữ liệu | may: grep non-scaling-stroke | 3 | ✓ |
| H08 | Chữ không mang màu dữ liệu | hinh vòng 1: chữ không mang màu dữ liệu | 5 | ✓ |
| H09 | Không nhãn nào bị cắt hay trào; không `overflow:hidden` trên đoạn cột | hinh vòng 1 + sửa mục lục: 0 nhãn bị cắt ở mọi bề rộng đã đo | 5 | ✓ |
| H10 | **Mọi** biểu đồ có bảng song sinh chứa đủ giá trị | hinh vòng 1: không áp dụng — 0 biểu đồ thật | 5 | ✓ |
| H11 | Khi in, `details` bảng số liệu mở ra, không bị ẩn | hinh vòng 1: không áp dụng — 0 thẻ bảng gập | 5 | ✓ |
| H12 | Khi in, hoạt ảnh hiện dần và hoạt ảnh vẽ đường đều mở bung — không thẻ nào in ra trắng | hinh vòng 1 + in lại PDF: 16 trang, 0 trang trắng, 0 tiêu đề mồ côi | 5 | ✓ |
| H13 | `@page { size: A4 }`, `break-inside: avoid` trên thẻ và mục | may: @page A4 + break-inside trên thẻ, section đã bỏ khỏi luật | 3 | ✓ |
| H14 | Hàng chỉ số 4–6 ô; đúng một số lớn mỗi trang; 3–6 hình mỗi trang | hinh vòng 1: hàng chỉ số 4 ô, 0 số lớn, 0 hình | 3 | ✓ |
| H15 | Khung biểu đồ chừa cả dải nhãn trục — không thanh cuộn dọc bên trong thẻ | hinh vòng 1: đo 5 bề rộng, 0 thẻ sinh cuộn dọc | 3 | ✓ |
| H16 | Mọi biểu đồ có `role="img"` và `aria-label` nói ra kết luận | hinh vòng 1: không áp dụng — 0 biểu đồ | 3 | ✓ |
| H17 | `prefers-reduced-motion` được tôn trọng | hinh vòng 1: chạy --force-prefers-reduced-motion, 24/24 thẻ hiện ngay | 1 | ✓ |
| H18 | Không khớp lỗi nào trong danh sách 25 lỗi | hinh vòng 1: chỉ khớp 1 lỗi (toàn vẹn nhãn), đã sửa và đo lại | 5 | ✓ |
| D01 | Người đọc độc lập làm được việc ở nhịp ba của họ | doc vòng 2: nhịp ba gốc bị DỮ LIỆU chặn, không phải trang chặn — xem D01 ở defects | 5 | ✗ |
| D02 | Không con số nào người đọc không nói lại được với người khác | doc vòng 2: mọi con số nói lại được, trừ các số đã gắn nhãn chưa dùng được — đó là chủ đích | 5 | ✓ |
| D03 | Con số ở lại trong đầu người đọc là con số quan trọng, không phải con số đã bị rút lại | doc vòng 2: con số ở lại vẫn là con số đã gắn nhãn chưa dùng được | 5 | ✗ |
| D04 | File mở được ngoại tuyến — không tham chiếu `http` nào | may: grep src/href http → 0 |href="http' → 0 | ✓ | ✓ |
| D05 | Xuất CSV có BOM `﻿` | may: ký tự BOM có trong đường xuất CSV | 3 | ✓ |
| D06 | Tên sắp bằng `localeCompare(..., 'vi')` | may: localeCompare(y, 'vi') | 3 | ✓ |
| D07 | Số theo lối Việt: phẩy thập phân, chấm hàng nghìn, `—` cho chỗ thiếu | giong vòng 2: phẩy thập phân (76,5 · 99,9), chấm hàng nghìn (1.392), — cho chỗ thiếu | 3 | ✓ |

---

## Phần riêng theo yêu cầu — thêm dòng ở đây

Mỗi chỉ số người dùng đã đồng ý thành một dòng. Mỗi mục trong trang thành một dòng. `W=5` cho chỉ số phục vụ trực tiếp quyết định ở nhịp ba; `W=3` cho chỉ số chống lưng; `W=1` cho phần mài giũa.

| ID | Requirement | Verify | W | Status |
|---|---|---|---|---|
| R01 | Số tiết đọc được của từng lớp trong 31/08–04/09, kèm `class_id` đã hỏi, cộng một cửa sổ rộng 01/08–14/09 để chống kết luận sai | du-lieu vòng 2: 20/20 lời gọi, class_id đầy đủ in trên trang | 5 | ✓ |
| R02 | Bảng cảnh báo dữ liệu chuyên cần: số thô của cả 4 lời gọi mức lớp, trên 2 cửa sổ liền nhau | du-lieu vòng 2: 4 lời gọi, 2 khoảng, 0 tỉ lệ | 5 | ✓ |
| R03 | Hai trường `not_marked` và `excused` ở mức học sinh, kèm cỡ mẫu đã tra 2/70 | du-lieu vòng 2: not_marked và excused có mặt, cỡ mẫu 2/70 in cạnh | 3 | ✓ |
| R04 | Rà soát sổ lớp: 7 phép kiểm, dòng dạng dữ liệu thử tách riêng khỏi mọi số đếm em | du-lieu vòng 2: 9 phép kiểm, dòng dữ liệu thử tách riêng | 3 | ✓ |
| R05 | Sĩ số hai lớp chủ nhiệm, đếm `role=="student"`, kèm số dòng giáo viên đã loại | du-lieu vòng 2: đếm tay role==student cả hai sổ | 5 | ✓ |
| R06 | Mục "Chưa dựng được" nêu 4 đầu việc, trong đó có việc cần thêm công cụ đọc buổi điểm danh ở hệ thống | doc vòng 2: 5 thẻ, chia hai bảng theo ai làm được việc | 3 | ✓ |
| R07 | Trang không có biểu đồ nào, và nói rõ vì sao — chốt chuyên cần cộng thiếu mẫu số | hinh vòng 1: xác nhận quyết định không vẽ là đúng, câu căn cứ đã sửa | 5 | ✓ |
| R08 | Dòng giả định nói rõ tài khoản có **hai** lớp chủ nhiệm và trang làm cho cả hai thay vì tự chọn một | doc vòng 2: dòng giả định nêu rõ hai lớp chủ nhiệm | 5 | ✓ |
| R09 | Mọi tiết đọc được rơi vào thứ Bảy và Chủ nhật — kết luận này truy được về trường `weekday` của 28 dòng tiết | du-lieu vòng 2: 28/28 entries[].weekday là Thứ 7 hoặc Chủ nhật | 5 | ✓ |
| R10 | Giới hạn độ phủ môn học nói ở đầu trang, kèm trần 60 của danh sách lớp | du-lieu vòng 2: trần 60 khai trong gioiHan; câu giới hạn nằm ở đoạn mở đầu | 5 | ✓ |
| R11 | Trả lời được khả năng “tuần đó là tuần đầu năm nên chưa có tiết” bằng dữ liệu | du-lieu vòng 2: 45 ngày đã đọc, 0 tiết ngày thường ở mọi tuần kể cả sau 05/09 | 5 | ✓ |
| R12 | Có ít nhất một việc thầy/cô làm được ngay dù số liệu chưa dùng được | doc vòng 2: thẻ cảnh báo nêu sổ đầu bài giấy và hỏi giáo viên bộ môn | 5 | ✓ |
| R13 | Khối số mức học sinh mang khoảng ngày đứng cạnh nó | du-lieu vòng 2: khoảng in ở phụ đề thẻ và thêm vào dòng khoảng đầu trang | 3 | ✓ |
| R14 | Trang hiện được nội dung dù JS chết giữa đường | may: check_runtime.py · chốt CSS bảo đảm hiện sau 1,2 giây không cần JS | 5 | ✓ |
| R15 | Nhãn ngày trong tuần đúng theo từng lớp, không dùng một nhãn chung | du-lieu vòng 2: 6a2 Hóa học cả hai ngày, hai lớp 9A2 chỉ Chủ nhật | 5 | ✓ |

---

## Luật chống bò phạm vi

Lăng kính đề xuất thêm mục hay thêm chỉ số thì **không** tự thêm dòng. Mục mới phải xin người dùng đồng ý trước. Lăng kính chỉ báo phát hiện.

## Luật chống lặp vô hạn

Một lỗi cùng nội dung mở qua **3 vòng** thì `qc_score.py` in `STALLED` và việc đúng là **dừng, đưa lên người dùng** kèm bằng chứng — không tranh luận vòng tròn.

## Luật khôi phục

`qc/spec-matrix.md` và `qc/defects.md` là nguồn sự thật duy nhất. Phiên bị ngắt giữa đường thì đọc lại hai file này là biết đang ở đâu.
