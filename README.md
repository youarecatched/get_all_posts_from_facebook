Mongodb: Tạo database facebook và collection post

Các bước chạy code:
1. run file get_all_post_from_fb.py để lấy posts từ trang cá nhân facebook dựa vào token.
2. run file posts_api để start server api truy vấn posts.

Ví dụ:
Sử dụng curl để post dữ liệu.
cú pháp: curl -X POST "http://localhost:3000/posts/search?q=sinh"

kết quả:
{
  "data": [
    {
      "content": "Sinh nhật zui zẻ hông quạu nha anh Bùi Minh Hòa !!"
    }
  ]
}
