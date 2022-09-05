import './App.css';
import {Card, H1, Button} from "@blueprintjs/core";
import UserInput from "./components/UserInput";
import Test from "./components/Test";
import GradePlot from "./components/GradePlot";



function App() {
  return (
    <div className={"main"}>

      <Card
        className={"header"}
        interactive={false}
        elevation={2}
        style={{backgroundColor: "#500000"}}
        onClick={() => console.log("clicked")}
      >
        <H1 style={{color: "white"}}>TAMU Grade Distribution</H1>
      </Card>

      <div className={"main"}>
        <UserInput/>
      </div>


    </div>
  );
}

export default App;
