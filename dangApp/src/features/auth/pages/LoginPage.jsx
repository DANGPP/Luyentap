// src/features/auth/pages/LoginPage.jsx
import {
  Button,
  Container,
  TextField,
  Typography,
  Box

} from "@mui/material";
import { useState, useEffect, useRef } from 'react'
import { Link } from 'react-router-dom'
import axios from "axios"

function LoginPage() {

  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const [logined, setLogined] = useState(false)
  const [message, setMessage] = useState("")

  const handleEmail = (event) => {
    setEmail(event.target.value.trim())
  }

  const handlePassword = (event) => {
    setPassword(event.target.value).trim()

  }

  const handleLogin = async (e) => {
    setLogined(true)
    e.preventDefault();
    if (email !== "" && password !== "") {
      try {
        const res = await axios.post("http://localhost:5000/api/login", {
          email,
          password
        });
        if (res.status === 200) {
          const { access_token, user, type } = res.data;
          const msg = `Xin chào ${user.hovaten}, bạn đã đăng nhập thành công`;
          alert(msg)
          setMessage(msg)
        } else {
          alert("Sai tên đăng nhập hoặc mật khẩu")
        }
      } catch (err) {
        setMessage(err)
        if (err.response) {
          // Server có trả lời nhưng mã lỗi (ví dụ 401)
          alert(err.response.data.message || "Đăng nhập thất bại 2");
        } else {
          // Không kết nối được server
          alert("Lỗi kết nối server");
        }
      }
    }
  }

  return (
    <Container maxWidth="xs" sx={{ border: "2px dotted black", }} >
      <Box mt={10} sx={{ border: "2px solid black" }}>
        <Typography variant="h4" >
          Đăng nhập
        </Typography>
        <TextField fullWidth label="Email" margin="normal"
          onChange={(e) => { handleEmail(e) }}

        />
        <Typography color="red" sx={{ fontSize: 12, display: email == "" && logined == true ? "block" : "none" }}>Vui lòng nhập email </Typography>
        <TextField fullWidth label="Mật khẩu" type="password" margin="normal"
          onChange={(e) => { handlePassword(e) }}
        />
        <Typography color="red" sx={{ fontSize: 12, display: password == "" && logined == true ? "block" : "none" }}>Vui lòng nhập mật khẩu</Typography>

        <Button fullWidth variant="contained" sx={{ mt: 2 }}
          onClick={handleLogin}
        >
          Đăng nhập
        </Button>
      </Box>
      <Typography mt={5}>Bạn chưa có tài khoản?<Link to="/register">Đăng ký</Link></Typography>
    </Container>
  );
}
export default LoginPage;
