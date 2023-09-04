import AppCSS from './index.module.css';
import {useState} from "react";

function App() {


  const [Input, setInput] = useState("");

  const [result, setResult] = useState();


  async function onSubmit(event){

      event.preventDefault();
      try{

        const message = encodeURIComponent(Input);

        const response = await fetch(`http://127.0.0.1:5000/api/generator/${message}`, {

            method: "GET",
            headers:{
              "Content-Type": "application/json",
            },
        });

        console.log(response.status)
        console.log(response.ok)
        if (!response.ok) {
          throw new Error(`Request failed with status ${response.status}`);
        }
        console.log(response.ok)

        const response_data = await response.json();
  
        console.log(response_data)
        if(response.status !== 200){
          throw new Error(`Request failed with status ${response.status}`);
        }
        console.log("changing state!")
        setResult(response_data.result);

        setInput("");

      }catch(error){

      }

  }
  


  return (
    <div className="App">
      <header className="App-header">
        <title> Ask About Me!</title>
      </header>

      <main className={AppCSS.main}>

        <h2>Frank's Q&A Session!</h2>

        <form onSubmit={onSubmit}>

          <input type="text" name="input" value={Input} placeholder="Put your question here" onChange={(e)=>setInput(e.target.value)} />
            
          <input type="submit" value="Answer it!"/>

        </form>

        <div className={AppCSS.result}> {result} </div>

      </main>
    </div>
  );
}

export default App;
