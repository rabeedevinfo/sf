
        console.log("JavaScript is running");
document.getElementById("id_date_deb").addEventListener('blur', function() {
            // Call date_end function when the input loses focus
            date_end();
        });		
		
function compt(){
            // Wait until the DOM is fully loaded
            document.addEventListener("DOMContentLoaded", function () {
                // Safely attach event listeners when DOM is ready
                let dateDebField = document.getElementById("id_date_deb");
                if (dateDebField) {
                    dateDebField.addEventListener('blur', date_end());
                }
            });
        }
        // Define the date_end function before using it in event listeners
        function date_end(){
			
            // Get the values from the fields
            let numberpart = document.getElementById("id_number_part").value;
            let datedeb = document.getElementById("id_date_deb").value;
            
            // Set the value of the "id_date_fin" input field
            //document.getElementById("id_date_fin").value = datedeb + numberpart; // Using .value
        }
		
		

        

        // Call compt to initialize the event listener
        
    