import { useState } from "react";
import axios from "axios";

function Register() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();
    const res = await axios.post("http://localhost:8080/api/auth/register", {
      email,
      password,
    });
    alert(res.data);
  };

  return (
    <form onSubmit={handleRegister} className="p-4">
      <h2 className="text-xl">Register</h2>
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
      <button className="bg-blue-500 text-white p-2">Register</button>
    </form>
  );
}

export default Register;
