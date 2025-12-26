import './srcpagestyle/PersonalAcademicInfo.css';
import React, { useState } from "react";

// Ito ang main functional component
const PersonalAcademic = () => {
  // useState para mag-store ng mga input data ng user
  // formData ay isang object na may 5 fields: name, strand, gpa, school, email
  const [formData, setFormData] = useState({
    name: "",
    strand: "",
    gpa: "",
    school: "",
    email: "",
  });

  // handleChange() – kapag may binago sa input field, dito papasok ang update
  // Destructure name at value mula sa event target (input element)
  const handleChange = (e) => {
    const { name, value } = e.target;
    // setFormData() – i-update ang state gamit ang spread operator (...formData)
    // para hindi mawala ang ibang fields habang ina-update lang ang isa
    setFormData({ ...formData, [name]: value });
  };

  // handleSubmit() – Dito naman nag rurun yung mga sinubmit o pinasa ng user
  const handleSubmit = (e) => {
    e.preventDefault(); // I-stop ang default behavior ng form (page reload)
    console.log("Submitted Data:", formData); // I-print sa console ang form data
    alert("Student information submitted successfully!"); // may notif para sa student na naipasa na or nai-submit yung data nya
    localStorage.setItem("personalAcademicData", JSON.stringify(formData)); //Dito muna sa "localStorage" ma-sasave para magamit sa SituationalQuest page baguhin mo nalang to kapag may backend na ng API call
  };

  return (
    <div className="student-form-container">
      <h2>Student Academic Information</h2>

      
      <form onSubmit={handleSubmit} className="student-form"> {/* Form element na magta-trigger ng handleSubmit kapag sinumite */}
        {/* Full Name Field */}
        <label>
          Full Name:
          <input type="text" name="name" placeholder="Enter your full name" 
            value={formData.name}     // Controlled input – value galing sa state
            onChange={handleChange}   // Tumatawag sa function kapag may nag-type
            required/>   
        </label>


        <label>
          Strand:
          <select
            name="strand" value={formData.strand}onChange={handleChange} required>
            <option value="">Select your strand</option>
            <option value="STEM">STEM</option>
            <option value="ABM">ABM</option>
            <option value="HUMSS">HUMSS</option>
            <option value="TVL">TVL</option>
            <option value="GAS">GAS</option>
          </select>
        </label>

        {/* Dito sila maglalagay ng grade */}
        <label>
          General Average (GPA):
          <input
            type="number"           
            step="0.01"               
            name="gpa"
            placeholder="example: 1.75"
            value={formData.gpa}
            onChange={handleChange}
            required
          />
        </label>

        {/* Dito sila maglalagay ng school name */}
        <label>
          School Name:
          <input
            type="text"
            name="school"
            placeholder="Enter your school name"
            value={formData.school}
            onChange={handleChange}
          />
        </label>

        {/* Email Address */}
        <label>
          Email Address:
          <input
            type="email"
            name="email"
            placeholder="Enter your email"
            value={formData.email}
            onChange={handleChange}/>
        </label>

        {/* Submit Button */}
        <button type="submit">Submit</button>


        {/*Skip Button*/}
        <button type="button" onClick={() => {console.log("User skipped the form");}}>Skip</button>
        
      </form>
    </div>
  );
};
export default PersonalAcademic;