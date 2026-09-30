# ths-bao-cao-mau

Đây là phần kiểm tra chất lượng còn lại sau một lần dựng báo cáo Trường học số bằng skill `ths-bao-cao`. Bản báo cáo đó trả lời một giáo viên chủ nhiệm: hai lớp mình chủ nhiệm đi học thế nào trong khoảng 31/08–04/09/2026. Repo chỉ giữ hai thứ dùng lại được cho báo cáo khác: một script kiểm trang lúc chạy và một bảng nghiệm thu mẫu. Bản báo cáo và nhật ký lấy số liệu nằm lại trên máy, vì có tên và mã học sinh thật.

Người làm: Bob (BobLe, bob@techainer.com), tháng 9/2026. Tình trạng: nguyên mẫu.

## Mở hoặc chạy thế nào

Script kiểm trang cần Python 3, thư viện Pillow và Chrome hoặc Edge cài ở đường dẫn mặc định.

```
pip install pillow
python qc/check_runtime.py duong-dan/toi/bao-cao.html
```

Mã trả về: 0 là sạch, 1 là có lỗi chặn, 2 là gọi sai cách hoặc không dựng được trang. Chạy lại ngày 30/09/2026 trên bản báo cáo gốc: 0 lỗi chặn.

Script làm ba phép, xếp từ chắc tới thô:

1. Ô rỗng: ô dựng sẵn trong trang mà không đoạn mã nào điền vào. Lỗi giữa chừng luôn để lại dấu ở đây.
2. Lỗi lúc chạy: đọc console của trình duyệt, bắt các dòng `Uncaught TypeError`, `ReferenceError`...
3. Vùng trắng: chụp ảnh trang rồi đo độ chênh màu ở hai dải ngang. Phép này đo cả nền, nên đừng kết luận chỉ dựa vào nó.

Bảng nghiệm thu `qc/spec-matrix.md` mở bằng trình xem Markdown nào cũng được. Cột Status: `✓` đã kiểm, `~` đã làm nhưng chưa kiểm, `✗` còn mở.

## Trong repo có gì

| File | Để làm gì |
|---|---|
| `qc/check_runtime.py` | Mở trang báo cáo bằng trình duyệt chạy ngầm, xem trang có thật sự hiện chữ không |
| `qc/spec-matrix.md` | Bảng nghiệm thu 68 yêu cầu của bản báo cáo chuyên cần, mỗi dòng ghi ai kiểm và kiểm bằng gì |
| `.gitignore` | Chặn báo cáo HTML, file xuất CSV/PDF/ảnh và hai file QC có dữ liệu học sinh |

Script ra đời từ một lỗi thật. Một bản báo cáo vỡ giữa đoạn mã, mở ra gần như trắng. Hai máy dò cũ của skill vẫn báo đạt, vì chúng chỉ soi nội dung đã dựng chứ không xem trang có hiện lên không.

## Dữ liệu

Repo không có số liệu học sinh. Bảng nghiệm thu chỉ nhắc tên lớp (6a2, Lớp 9A2) và số đếm, không có tên em nào.

Báo cáo gốc dựng từ dữ liệu thật của Trường học số, đọc qua MCP bằng tài khoản giáo viên và tài khoản quản trị trường. Chỉ dùng lời gọi đọc, không ghi gì vào hệ thống.

## Không có trong repo

| File để lại trên máy | Vì sao |
|---|---|
| `2026-09-08-2-lop-chu-nhiem-di-hoc.html` | Bản báo cáo chính. Có tên giáo viên, tên và mã định danh học sinh |
| `qc/mcp-log.md` | Nhật ký từng lời gọi MCP. Có sổ lớp, tên em kèm mã và số lượt vắng |
| `qc/defects.md` | Sổ lỗi 83 dòng. Vài dòng nêu tên học sinh cạnh số điểm danh |

Ba file này vẫn ở thư mục `bao-cao` trên máy của Bob. Ai cần thì chuyển qua kênh nội bộ, không đưa lên chỗ công khai.

## Lưu ý cho người nhận

- `check_runtime.py` chưa được gộp vào skill `ths-bao-cao`. Skill nằm ở `~/.claude/skills/ths-bao-cao/`, ngoài repo này. Trong sổ lỗi, việc gộp vẫn ghi là còn mở.
- `spec-matrix.md` được `scripts/qc_score.py` của skill đọc để chấm điểm. Muốn dùng làm mẫu thì giữ đúng năm cột, đúng thứ tự.
- Đừng đo bằng lớp CSS `.reveal.in`. Cùng một file cho 0/27 rồi 8/27 giữa hai lần chạy, vì bộ theo dõi cuộn không ổn định khi trình duyệt chạy ngầm. Script chỉ in số đó để tham khảo.
- Ngưỡng 120 của phép vùng trắng đo trên đúng một bản báo cáo. Trang có nền khác thì nên đo lại.
- Pillow đang cảnh báo hàm `getdata` sẽ bị bỏ ở Pillow 14 (khoảng tháng 10/2027). Tới lúc đó đổi sang `get_flattened_data`.
- Bảng nghiệm thu còn hai dòng mở (D01, D03). Việc giáo viên cần nhất là danh sách em nghỉ ngày nào. Việc này chưa làm được, vì số liệu điểm danh khoảng đó ghi vắng gần như mọi dòng. Đó là chuyện dữ liệu hệ thống, chưa ai xác nhận nguyên nhân.
