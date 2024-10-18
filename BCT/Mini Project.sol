// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "hardhat/console.sol";

struct Patient {
    int patient_id;
    string name;
    string height;
    string weight;
    string disease;
    string symptom1;
    string symptom2;
}

contract Health_Record {

    Patient[] private Patients;

// Add a new patient record or update if ID exists
    function addPatient(
        int patient_id, 
        string memory name, 
        string memory height, 
        string memory weight, 
        string memory disease, 
        string memory symptom1, 
        string memory symptom2
    ) public returns (bool) {
        // First check if patient with this ID already not exists
        for (uint i = 0; i < Patients.length; i++) {
            if (Patients[i].patient_id == patient_id) {
                console.log("Patient Exists");
                return false;
            }
        }
        
        // patient doesn't exist, so add new record
        Patient memory patient = Patient(
            patient_id,
            name,
            height,
            weight,
            disease,
            symptom1,
            symptom2
        );
        Patients.push(patient);
        return true; // Return false to indicate new record was created
    }


    function getPatientCount() public view returns (uint256){
        uint256 l = Patients.length;
        return l;
    }

    // Retrieve patient details by patient_id
    function getPatient(int patient_id) public view returns (string memory, string memory, string memory, string memory, string memory, string memory) {
        for (uint i = 0; i < Patients.length; i++) {
            if (Patients[i].patient_id == patient_id) {
                return (
                    Patients[i].name,
                    Patients[i].height,
                    Patients[i].weight,
                    Patients[i].disease,
                    Patients[i].symptom1,
                    Patients[i].symptom2
                );
            }
        }
        return ("Name not Found", "Height not Found", "Weight not Found", "Disease not Found", "Symptom1 not Found", "Symptom2 not Found");
    }

    // update record
    function updatePatient(
        int patient_id,
        string memory name,
        string memory height,
        string memory weight,
        string memory disease,
        string memory symptom1,
        string memory symptom2
    ) public returns (bool) {
        for (uint i = 0; i < Patients.length; i++) {
            if (Patients[i].patient_id == patient_id) {
                Patients[i].name = name;
                Patients[i].height = height;
                Patients[i].weight = weight;
                Patients[i].disease = disease;
                Patients[i].symptom1 = symptom1;
                Patients[i].symptom2 = symptom2;
                return true;
            }
        }
        return false;
    }

    // Delete patient record by patient_id
    function deletePatient(int patient_id) public returns (bool) {
        for (uint i = 0; i < Patients.length; i++) {
            if (Patients[i].patient_id == patient_id) {
                // Move the last element to the position of the element to delete
                if (i != Patients.length - 1) {
                    Patients[i] = Patients[Patients.length - 1];
                }
                // Remove the last element
                Patients.pop();
                return true;
            }
        }
        return false;
    }
}