// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    // Structure to store student information
    struct Student {
        string name;
        uint256 age;
        uint256 id;
    }

    // Dynamic array to store students (private)
    Student[] private students;

    // Event to emit when a student is added
    event StudentAdded(string name, uint256 age, uint256 id);

    // Function to add a new student
    function addStudent(string memory _name, uint256 _age, uint256 _id) public {
        Student memory newStudent = Student({
            name: _name,
            age: _age,
            id: _id
        });
        
        students.push(newStudent);
        emit StudentAdded(_name, _age, _id);
    }

    // Function to retrieve student information by index
    function getStudent(uint256 index) public view returns (string memory, uint256, uint256) {
        require(index < students.length, "Student does not exist.");
        Student memory student = students[index];
        return (student.name, student.age, student.id);
    }

    // Function to get the total number of students
    function getTotalStudents() public view returns (uint256) {
        return students.length;
    }

    // Fallback function to receive Ether
    receive() external payable {
        // Fallback function can be used to accept ether
    }
}
