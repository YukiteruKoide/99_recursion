function answerIs(self, expected) {
    if (self.value === "") {
        self.style.backgroundColor="#ffffff";
    } else if (self.value.toLowerCase().includes(expected)) {
        self.style.backgroundColor="#7ffe78";
    } else {
        self.style.backgroundColor="#ffb9bb";
    }
}

function loaded() {
    const catalog_name = localStorage.getItem("gswds_catalog_name");
    const username = localStorage.getItem("gswds_username");
    if (catalog_name) {
        document.getElementById("catalog_name").value = catalog_name;
    }
    if (username) {
        document.getElementById("username").value = username;
    }
    update();
}

function update() {      
    let catalog_name = document.getElementById("catalog_name").value;
    let username = document.getElementById("username").value;
    let ids = ['step-1', 'step-2', 'step-3', 'step-4'];

    if (catalog_name === null || username === null || 
        catalog_name === "" || username === "" || 
        catalog_name == "n/a" || username === "n/a") {
        for (let i = 0; i < ids.length; i++) {
            document.getElementById(ids[i]+"-test-ta").disabled = true;
            document.getElementById(ids[i]+"-sql-ta").disabled = true;

            document.getElementById(ids[i]+"-test-btn").disabled = true;
            document.getElementById(ids[i]+"-sql-btn").disabled = true;

            document.getElementById(ids[i]+"-test-ta").value = document.getElementById(ids[i]+"-test-backup").value
            document.getElementById(ids[i]+"-sql-ta").value = document.getElementById(ids[i]+"-sql-backup").value
        }
    } else if (catalog_name == "n/a" || username === "n/a") {
        for (let i = 0; i < ids.length; i++) {
            document.getElementById(ids[i]+"-test-ta").disabled = false;
            document.getElementById(ids[i]+"-sql-ta").disabled = false;

            document.getElementById(ids[i]+"-test-btn").disabled = false;
            document.getElementById(ids[i]+"-sql-btn").disabled = false;
        }    
    } else {
        let illegals = ["<",">","\"","'","\\","/"]; 
        for (let i= 0; i < illegals.length; i++) {
            if (catalog_name.includes(illegals[i])) {
                alert("Please double check your catalog name.\nIt cannot not include the " + illegals[i] + " symbol.");
                return;
            }
            if (username.includes(illegals[i])) {
                alert("Please double check your username.\nIt cannot not include the " + illegals[i] + " symbol.");
                return;
            }
        }
        if (catalog_name.includes("@")) {
            alert("Please double check your catalog name.\nIt should not include the @ symbol.");
            return;
        }
        if (username.includes("@") === false) {
            alert("Please double check your username.\nIt should include the @ symbol.");
            return;
        }
        
        document.getElementById("catalog-input-msg").innerText = catalog_name;
        document.getElementById("username-input-msg").innerText = username;
        
        for (let i = 0; i < ids.length; i++) {
            document.getElementById(ids[i]+"-test-ta").disabled = false;
            document.getElementById(ids[i]+"-sql-ta").disabled = false;

            document.getElementById(ids[i]+"-test-btn").disabled = false;
            document.getElementById(ids[i]+"-sql-btn").disabled = false;

            document.getElementById(ids[i]+"-test-ta").value = document.getElementById(ids[i]+"-test-backup").value
                                                                       .replaceAll("{catalog_name}", catalog_name)
                                                                       .replaceAll("{username}", username);

            document.getElementById(ids[i]+"-sql-ta").value = document.getElementById(ids[i]+"-sql-backup").value
                                                                      .replaceAll("{catalog_name}", catalog_name)
                                                                      .replaceAll("{username}", username);

            localStorage.setItem("gswds_catalog_name", catalog_name);
            localStorage.setItem("gswds_username", username);
        }
        console.log(localStorage.getItem("gswds_username"));
    }
}
