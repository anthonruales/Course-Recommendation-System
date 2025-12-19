// Replace your current handleSubmit in Signup.js with this:
const handleSubmit = async (e) => {
  e.preventDefault();
  console.log("Sending data:", formData); // CHECK YOUR BROWSER CONSOLE
  try {
    const response = await axios.post('http://localhost:8000/signup', {
      fullname: formData.fullname,
      email: formData.email,
      password: formData.password
    });
    alert("Registration Successful!"); 
    onSwitch();
  } catch (err) {
    // This will tell us EXACTLY what the backend said
    console.error("Signup Error Details:", err.response?.data);
    alert(err.response?.data?.detail || "Error during signup.");
  }
};