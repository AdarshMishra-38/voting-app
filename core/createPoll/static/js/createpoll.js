const AddFieldbtn = document.querySelector("#add-field");
const FieldContainer = document.querySelector("#field-container")
const AppendedField =  document.querySelector("#append-field")
const CreatePollFrom = document.querySelector("#create-poll-form")
const PollFormBtn =  document.querySelector("#Create-poll-form-submit-btn")
// console.log(AppendedField)
let fieldno = 1;
const FormDataObj = {};


AddFieldbtn.addEventListener('click',AppendField);

function AppendField(){
    fieldno++;
    FieldContainer.innerHTML+=` <div class="mb-1 p-3" id="append-field" >
    <label  class="form-label" for="field-${fieldno}">field</label><span> ${fieldno}:</span>
    <input type="text" class="form-control"  name="field-${fieldno}" class= "fields">
  </div>
`;


// console.log("field added")

}



// function FetchFormData(event){
//     // event.preventDefault();
//     let formdata = new FormData(CreatePollFrom);
//     for (const pair of formdata.entries()) {
//         FormDataObj[pair[0]]=pair[1];
        
//     }
    // console.log(FormDataObj)


    // return FormDataObj;
    
// }

// PollFormBtn.addEventListener("click", ()=>{
//     FetchFormData();
//     console.log(FormDataObj)
//     alert("form has been successfully submitted")
// })


// export {FetchFormData, PollFormBtn, CreatePollFrom}; 