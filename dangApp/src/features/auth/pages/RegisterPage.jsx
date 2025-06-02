import {
    Button,
    Container,
    TextField,
    Typography,
    Box
} from "@mui/material"
import { Link } from "react-router-dom";
import { useState } from "react";
import axios from "axios";

function RegisterPage() {
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [confirmPassword, setConfirmpassword] = useState("")
    const [hovaten, setHovaten] = useState("")
    const [ngaysinh, setNgaysinh] = useState("")
    const [sdt, setSdt] = useState("")
    const [tennganhang, setTennganhang] = useState("")
    const [stknh, setStknh] = useState("")
    const [registered, setRegistered] = useState(false)

    const handleEmail = (e) => {
        setEmail(e.target.value.trim());
    }


    const handlePassword = (e) => {
        setPassword(e.target.value.trim());
    }


    const handleConfirmPassword = (e) => {
        setConfirmpassword(e.target.value.trim());
    }
    const handleHovaten = (e) => setHovaten(e.target.value.trim());
    const handleNgaysinh = (e) => setNgaysinh(e.target.value.trim());
    const handleSdt = (e) => setSdt(e.target.value.trim());
    const handleTennganhang = (e) => setTennganhang(e.target.value.trim());
    const handleStknh = (e) => setStknh(e.target.value.trim());

    const handleRegister = async () => {
        setRegistered(true)
        if(email!=="" && password!==""&& confirmPassword!=="" && hovaten!=="" && ngaysinh!="" && sdt!=="" && tennganhang!=="" && stknh!=="" ){
            try{
                const res = await axios.post("http://localhost:5000/api/register",{
                    email: email,
                    password: password,
                    hovaten: hovaten,
                    ngaysinh: ngaysinh,
                    sdt: sdt,
                    tennganhang: tennganhang,
                    stknh: stknh

                })
                if(res.status===200){
                    const {NewUser, message} = res.data
                    alert(message)
                }
            } catch(err){
                alert(err.response.data.message)
            }
        }

    }

    const comparePass = () => {
        if (password.trim() == "" || confirmPassword.trim() == "") {
            return false
        }
        if (password !== confirmPassword) {
            return false
        }
        return true

    }

    return (
        <Container maxWidth="xs" sx={{ border: "2px dotted black" }}>
            <Box mt={10} sx={{ border: "2px solid black" }}>
                <Typography variant="h4" >
                    Đăng ký
                </Typography>

                <TextField label="Email" fullWidth margin="normal"
                    onChange={(e) => { handleEmail(e) }}
                ></TextField>
                <Typography sx={{fontSize: 12, color: "red", display: email === "" && registered === true ? "block" : "none" }}>* Vui lòng nhập email</Typography>
                <TextField label="Password" fullWidth margin="normal" type="password"
                    onChange={(e) => { handlePassword(e) }}
                ></TextField>
                <Typography sx={{fontSize: 12, color: "red", display: password === "" && registered === true ? "block" : "none" }}>* Vui lòng nhập password</Typography>

                <TextField label="Confirm password" fullWidth margin="normal" type="password"
                    onChange={(e) => { handleConfirmPassword(e) }}
                ></TextField>
                <Typography   sx={{fontSize: 12, color: "red", display: confirmPassword === "" && registered === true ? "block" : "none" }}>* Vui lòng nhập confirmPassword</Typography>
                {registered && password !== "" && confirmPassword !== "" && password !== confirmPassword && (
                    <Typography color="red">* Mật khẩu xác nhận không khớp</Typography>
                )}

                <TextField label="Họ và tên" fullWidth margin="normal"
                    onChange={(e) => { handleHovaten(e) }}
                ></TextField>
                <Typography sx={{fontSize: 12, color: "red", display: hovaten === "" && registered === true ? "block" : "none" }}>* Vui lòng nhập họ và tên</Typography>
                
                <TextField label="Ngày sinh" fullWidth margin="normal"
                    onChange={(e) => { handleNgaysinh(e) }}
                ></TextField>
                <Typography sx={{fontSize: 12, color: "red", display: ngaysinh === "" && registered === true ? "block" : "none" }}>* Vui lòng nhập ngày sinh</Typography>

                <TextField label="Số điện thoại" fullWidth margin="normal"
                    onChange={(e) => { handleSdt(e) }}
                ></TextField>
                <Typography sx={{fontSize: 12, color: "red", display: sdt === "" && registered === true ? "block" : "none" }}>* Vui lòng nhập số điện thoại</Typography>

                <TextField label="Tên ngân hàng" fullWidth margin="normal"
                    onChange={(e) => { handleTennganhang(e) }}
                ></TextField>
                <Typography sx={{fontSize: 12, color: "red", display: tennganhang === "" && registered === true ? "block" : "none" }}>* Vui lòng nhập tên ngân hàng</Typography>

                <TextField label="Số tài khoản ngân hàng" fullWidth margin="normal"
                    onChange={(e) => { handleStknh(e) }}
                ></TextField>
                <Typography sx={{fontSize: 12, color: "red", display: stknh === "" && registered === true ? "block" : "none" }}>* Vui lòng nhập số tài khoản ngân hàng</Typography>









                <Button fullWidth variant="contained"  sx={{ mt: 2 }}
                    onClick={handleRegister}
                >
                    Đăng ký
                </Button>
            </Box>
            <Typography marginTop={5}>
                Bạn đã có tài khoản? <Link to="/login">Đăng Nhập</Link>
            </Typography>
        </Container>
    );
}
export default RegisterPage;