<p><b>OOPs in python practice for BMW</b></p>

<p><b>Objective: To understand the OOPs concept and to get famillier with git and GitHub.</b></p>

<p>Follow below steps:-</p>
<ul>
  <li>fork this repository</li>
  <li>Clone the forked repo to your local machine</li>
  <li>Create a branch</li>
  <li>Write down the code</li>
  <li>Push the changes</li>
  <li>Create PR from Github UI</li>
</ul>
<br>
<p>Create Employee-Management-System which follows OOPs concepts.<br>Floder structure should be:</p>
<pre>
  Parent folder
    src
    test
  main.py
</pre>
<P>src should contains main logic and test should contain all the unittest cases along with the dummy data required for the success of unittest</P>

<p>Aim of Employee’s Management System:

  Data of the Employee’s
<ul>
  <li><b>Name</b></li>
  <li><b>Employee ID</b>(it should be auto fill)</li>
  <li><b>Designation</b>(Put by default DEV. and designation must be enum)</li>
  <li><b>Experience</b>(put by default fresher</li>
  <li><b>Age,</b></li>
  <li><b>Salary</b>(it should be autofill, for DEV. 40,000, for TL 40,000*2=80,000, for MNG. 40,000*3=1,20,000)</li>
  <li><b>skills</b>(This field is not required for MNG, atleast two skills must be added for DEV, and Atmost one skill for TL)</li>
</ul>
<br>
  Manager class inherets Emp class <br>
  Project Class
  <ul>
    <li>Project ID</li>
    <li>Project Title</li>
    <li>Skills required</li>
    <li>Deadline</li>
    <li>Discreption</li>
    <li>Project MNG</li>
  </ul>
  Functionallity
  <ul>
    <li>Built The Employee Table.</li>
    <li>Insert New Entries.</li>
    <li>Delete a Emp by ID.</li>
    <li>Search A Record by ID.</li>
    <li>Search A Record by Name.</li>
    <li>Search all Records by designation.</li>
    <li>Search emp by project</li>
    <li>Get all emp under paticular project</li>
    <li>Get all emp under particular MNG</li>
    <li>get all the emp who are on beanch</li>
    <li>Option to add skills to EMP</li>
    <li>Get salary</li>
    <li>Add a MNG</li>
  </ul>

<i><b>NOTE:</b>There should be a function which will execute when an employee is created, it should autometically assign a team, if adding a MNG then, it should ask you for Project Name and a project(class) should be created, if adding TL then according to project requirement TL should be added to project and if you are adding DEV then according to skills of DEV and requirement in project DEV should ne added to project. There can only be 5 DEV 1 TL and 1 MNG in a project. IF there is no project available and you are adding a EMP the put that EMP on beanch, if new project define then fist it should add EMP from beanch, there can only 5 MNG and all project should be equally divided among MNG, No duplicate projects, </i>
</p>

<p>Test coverage should be 100%<br>Code should be modular<br>Please use black formatter python extension to format the python code<br>Same type of entity/functionality must be in same class.</p>
