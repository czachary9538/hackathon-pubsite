function submitRegister() {
    Array.from(document.getElementsByClassName("error")).forEach((element) => element.remove());
    let failed = false;
    let firstName = document.getElementById("first_name").value;
    failed = pleaseFillIn(firstName, "first-div") || failed;
    let lastName = document.getElementById("last_name").value;
    failed = pleaseFillIn(lastName, "last-div") || failed;
    let email = document.getElementById("email").value;
    failed = pleaseFillIn(email, "email-div") || failed;
    let age = document.getElementById("age").value;
    failed = pleaseFillIn(age, "age-div") || failed;
    let phoneNumber = document.getElementById("phone_number").value;
    failed = pleaseFillIn(phoneNumber, "phone-div") || failed;
    let university = document.getElementById("university-dropdown").value;
    failed = pleaseFillIn(university, "uni-div") || failed;
    let shirtSize = document.getElementById("tshirt-dropdown").value;
    failed = pleaseFillIn(shirtSize, "tshirt-div") || failed;
    let currentStudyLevel = document.getElementById("studylevel-dropdown").value;
    failed = pleaseFillIn(currentStudyLevel, "study-div") || failed;
    let country = document.getElementById("country-dropdown").value;
    failed = pleaseFillIn(country, "country-div") || failed;
    let mlh1 = document.getElementById("mlh-checkbox-1").checked;
    if (!mlh1) {
        let mlh_button = document.getElementById("mlh-div-1");
        mlh_button.insertAdjacentHTML("beforebegin", 
        `
        <div class="alert alert-danger error" role="alert">
            Please agree to the following term(s).
        </div>
        `);
        failed = true;
    }
    let mlh2 = document.getElementById("mlh-checkbox-2").checked;
    if (!mlh2) {
        let mlh_button = document.getElementById("mlh-div-2");
        mlh_button.insertAdjacentHTML("beforebegin", 
        `
        <div class="alert alert-danger error" role="alert">
            Please agree to the following term(s).
        </div>
        `);
        failed = true;
    }
    let mlh3 = document.getElementById("mlh-checkbox-3").checked;
    if (!mlh3) {
        let mlh_button = document.getElementById("mlh-div-3");
        mlh_button.insertAdjacentHTML("beforebegin", 
        `
        <div class="alert alert-danger error" role="alert">
            Please agree to the following term(s).
        </div>
        `);
        failed = true;
    }
    let dietary = Array.from(document.getElementById("dietary-div").getElementsByTagName("input")).filter((element) => element.checked).map((element, index, array) => element.value);
    let dietaryOther = document.getElementById("dietary-other-text").value;
    let underrep = Array.from(document.getElementById("underrep-div").getElementsByTagName("input")).filter((element) => element.checked).map((element, index, array) => element.value);
    failed = pleaseFillIn(underrep, "underrep-div") || failed;
    let gender = Array.from(document.getElementById("gender-div").getElementsByTagName("input")).filter((element) => element.checked).map((element, index, array) => element.value);
    failed = pleaseFillIn(country, "country-div") || failed;
    let pronouns = Array.from(document.getElementById("pronouns-div").getElementsByTagName("input")).filter((element) => element.checked).map((element, index, array) => element.value);
    failed = pleaseFillIn(pronouns, "pronouns-div") || failed;
    let pronounsOther = document.getElementById("pronouns-other-text").value;
    let race = Array.from(document.getElementById("race-div").getElementsByTagName("input")).filter((element) => element.checked).map((element, index, array) => element.value);
    failed = pleaseFillIn(race, "race-div") || failed;
    let raceOther = document.getElementById("race-other-text").value;
    let orientation = Array.from(document.getElementById("orientation-div").getElementsByTagName("input")).filter((element) => element.checked).map((element, index, array) => element.value);
    failed = pleaseFillIn(orientation, "orientation-div") || failed;
    let orientationOther = document.getElementById("orientation-other-text").value;
    let highestEdu = Array.from(document.getElementById("edu-div").getElementsByTagName("input")).filter((element) => element.checked).map((element, index, array) => element.value);
    failed = pleaseFillIn(highestEdu, "edu-div") || failed;
    let eduOther = document.getElementById("edu-other-text").value;
    let major = Array.from(document.getElementById("major-div").getElementsByTagName("input")).filter((element) => element.checked).map((element, index, array) => element.value);
    failed = pleaseFillIn(major, "major-div") || failed;
    let majorOther = document.getElementById("major-other-text").value;
    let photo = Array.from(document.getElementById("photo-div").getElementsByTagName("input")).filter((element) => element.checked).map((element, index, array) => element.value);
    failed = pleaseFillIn(photo, "photo-div") || failed;

    let outJson = {
        firstName,
        lastName,
        email,
        age,
        phoneNumber,
        university,
        shirtSize,
        currentStudyLevel,
        country,
        mlh1,
        mlh2,
        mlh3,
        dietary,
        underrep: underrep[0],
        gender: gender[0],
        pronouns: pronouns[0],
        race,
        orientation,
        highestEdu: highestEdu[0],
        major,
        photo: photo[0]
    };
    if (pronouns.includes("other")) {
        failed = pleaseFillInOther(pronounsOther, "pronouns-div") || failed;
        outJson.pronounsOther = pronounsOther;
    }
    if (race.includes("other")) {
        failed = pleaseFillInOther(raceOther, "race-div") || failed;
        outJson.raceOther = raceOther;
    }
    if (orientation.includes("other")) {
        failed = pleaseFillInOther(orientationOther, "orientation-div") || failed;
        outJson.orientationOther = orientationOther;
    }
    if (highestEdu.includes("other")) {
        failed = pleaseFillInOther(eduOther, "edu-div") || failed;
        outJson.eduOther = eduOther;
    }
    if (major.includes("other")) {
        failed = pleaseFillInOther(majorOther, "major-div") || failed;
        outJson.majorOther = majorOther;
    }
    if (dietary.includes("other")) {
        failed = pleaseFillInOther(dietaryOther, "dietary-div") || failed;
        outJson.dietaryOther = dietaryOther;
    }

    if (failed) {
        document.getElementById("submit-div").insertAdjacentHTML("beforebegin", 
        `
        <div class="alert alert-danger error" role="alert">
            Failed to submit form. See above error(s),
        </div>
        `);
        document.getElementById("submit-div").scrollIntoView();
        return false;
    }
    console.log(JSON.stringify(outJson));
    fetch(
        "/register",
        {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(outJson)
        }
    ).then((resp) => {
        if (resp.status != 200) {
            document.getElementById("submit-div").insertAdjacentHTML("beforebegin", 
            `
            <div class="alert alert-danger error" role="alert">
                An error has occured on submission. Please try again later or contact hacks@csh.rit.edu
            </div>
            `);
            return false;
        } else {
            return resp.text();
        }
    }).then((text) => {
        if (text) {
            window.location.href = `/success?id=${text}`
        }
    }).catch((_) => {
        document.getElementById("submit-div").insertAdjacentHTML("beforebegin", 
            `
            <div class="alert alert-danger error" role="alert">
                An error has occured on submission. Please try again later or contact hacks@csh.rit.edu
            </div>
            `);
    });
    return false;
}

function pleaseFillIn(checkItem, div) {
    console.log(div);
    console.log(checkItem.length);
    if (checkItem.length == 0) {
        console.log(div);
        let question_field = document.getElementById(div);
        question_field.insertAdjacentHTML("beforebegin", 
        `
        <div class="alert alert-danger error" role="alert">
            Please fill in this section.
        </div>
        `);
        return true;
    }
    return false;
}

function pleaseFillInOther(checkOtherItem, div) {
    if (!checkOtherItem) {
        console.log(div);
        let question_field = document.getElementById(div);
        question_field.insertAdjacentHTML("beforebegin", 
        `
        <div class="alert alert-danger error" role="alert">
            Please fill in the "Other" text box.
        </div>
        `);
        return true;
    }
    return false;
}