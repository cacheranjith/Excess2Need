import { useState } from "react";
import axios from "axios";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    const res = await axios.post("http://localhost:8080/api/auth/login", {
      email,
      password,
    });
    alert("Token: " + res.data);
    localStorage.setItem("token", res.data);
  };

  return (
    <form onSubmit={handleLogin} className="p-4">
      <h2 className="text-xl">Login</h2>
      <input
        type="email"
        placeholder="Email"
        className="border p-2 m-2"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        className="border p-2 m-2"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button className="bg-green-500 text-white p-2">Login</button>
    </form>
  );
}

export default Login;
