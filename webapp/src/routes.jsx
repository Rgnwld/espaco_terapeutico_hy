import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";

function Project_Routes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
      </Routes>
    </BrowserRouter>
  );
}

export default Project_Routes;
