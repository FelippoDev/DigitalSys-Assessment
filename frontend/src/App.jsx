import { useState } from "react";
import "./App.css";
import { useEffect } from "react";
import ClipLoader from "react-spinners/ClipLoader";
import React from "react";
import InformIcon from "@mui/icons-material/PriorityHigh";
import CloseIcon from "@mui/icons-material/Close";
import { getRequiredFields, createLoanProposal } from "./services/external_apy";

function App() {
  const [fields, setFields] = useState(null);
  const [modal, setModal] = useState(false);

  function closeModal() {
    setModal(false);
  }

  async function submitForm(e) {
    e.preventDefault();
    let inputData = {
      proposal_amount: e.target.proposal_amount.value,
      fullname: e.target.fullname?.value,
      email: e.target.email?.value,
      document_number: e.target.document_number.value,
      phone_number: e.target.phone_number?.value,
    };
    let form = document.getElementById("form")
    form.reset()
    let response = await createLoanProposal(inputData);
    if (response.status === 201) {
      setModal(true);
    }
  }

  async function getFields() {
    const fields = await getRequiredFields();
    setFields(fields);
  }

  useEffect(() => {
    getFields();
  }, []);

  if (fields === null) {
    return (
      <>
        <div className="loading-icon">
          <ClipLoader
            color={"#16536f"}
            loading={true}
            size={150}
            aria-label="Loading Spinner"
            data-testid="loader"
          />
        </div>
      </>
    );
  }

  return (
    <>
      {modal ? (
        <div className="modal">
          <InformIcon id="inform-icon" />
          <span>Solitação de empréstimo em análise.</span>
          <button onClick={() => closeModal()}>
            <CloseIcon />
          </button>
        </div>
      ) : null}
      <h1>Proposta de empréstimo</h1>
      <form
        id="form"
        onSubmit={(e) => {
          submitForm(e);
        }}
        className="input-form"
      >
        <input
          type="text"
          pattern="[0-9]+"
          placeholder="Número documento"
          name="document_number"
        />
        <input
          type="number"
          name="proposal_amount"
          placeholder="Valor"
          pattern="[0-9]+"
          inputMode="numeric"
        />
        {fields.map((field) => {
          return field.is_required ? (
            <input
              type="text"
              placeholder={field.field_name}
              name={field.field_name}
            />
          ) : null;
        })}
        <input type="submit" value="enviar" className="input-btn" />
      </form>
    </>
  );
}

export default App;
