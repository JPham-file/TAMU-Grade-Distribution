import {Button, InputGroup} from "@blueprintjs/core";
import {useState} from "react";
import GradePlot from "./GradePlot";

const UserInput = () => {
  const [department, setDepartment] = useState(true);
  const [data, setData] = useState(null);
  const [print, setPrint] = useState(false);

  const getData = (props) => {
    setData(props.target.value);
    setPrint(false);
  }

  const getDepartment = (props) => {
    setDepartment(props.target.value);
    setPrint(false);
  }

  return (
    <div>
      {print ? <h2> {department} : {data} </h2> : null}
      <p className={"inline-text"}>Department Name</p>

      <InputGroup
        type={"text"}
        className={"input-group"}
        asyncControl={true}
        placeholder="e.g. CSCE"
        small="small"
        fill={false}
        onChange={getDepartment}
      />

      <p className={"inline-text"}>Department number</p>
      <InputGroup
        type={"text"}
        className={"input-group"}
        asyncControl={true}
        placeholder="e.g. 121"
        small="small"
        fill={false}
        onChange={getData}
      />

      <Button
        text={"submit"}
        small={true}
        intent={"primary"}
        onClick={() => setPrint(true)}
      />

      {
        print ?
        <div>
          <GradePlot/>
        </div>
        :
        null
      }

    </div>
  )
}

export default UserInput;