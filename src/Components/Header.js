import { useState, useEffect } from "react"
import GraphHandler from "./GraphHandler"
const Header = () => {

    const [assignment, setAssignment] = useState('All')

    return (
        <div>
            <button onClick={()=>{
                setAssignment("One")
            }}>
                Assignment 1
            </button>
            <button onClick={()=>{
                setAssignment("Two")
            }}>
                Assignment 2
            </button>
            <button onClick={()=>{
                setAssignment("Three")
            }}>
                Assignment 3
            </button>

            <button onClick={()=>{
                setAssignment("All")
            }}>
                All
            </button>

            <GraphHandler asn={assignment}/>
            
        
        
        </div>
    )
}

export default Header;