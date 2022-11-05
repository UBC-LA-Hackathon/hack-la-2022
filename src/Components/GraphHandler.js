import { Component, useEffect, useState } from "react";
import Papa from "papaparse";
import { getSystemErrorMap } from "util";
import csv from "../Data/gradebook.csv"

import {  
    XYPlot,
    XAxis,
    YAxis,
    VerticalGridLines,
    HorizontalGridLines,
    VerticalRectSeries,
    VerticalRectSeriesCanvas
} from "react-vis";



// asn -- assignment
const GraphHandler = ({asn}) => {

    const fetchCsv = () => {
        return fetch("https://cors-anywhere.herokuapp.com/https://raw.githubusercontent.com/UBC-LA-Hackathon/hack-la-2022/main/data/additional/gradebook.csv",
            {headers: { 'content-type': 'text/csv;charset=UTF-8'}}
        ).then((response) => response.text()
        ).then((data) => {
            console.log(data);
        });
    }
    const init = () => {

        Papa.parse("https://cors-anywhere.herokuapp.com/https://raw.githubusercontent.com/UBC-LA-Hackathon/hack-la-2022/main/data/additional/gradebook.csv", {
            download: true,
            header: true,
            skipEmptyLines: true,
            complete: function (results) {
                console.log(results);
                const rowsArray = [];
                const valuesArray = [];

                // Iterating data to get column name and their values
                results.data.map((d) => {
                    rowsArray.push(Object.keys(d));
                    valuesArray.push(Object.values(d));
                });

                // Parsed Data Response in array format
                setParsedData(results.data);

                // Filtered Column Names
                setTableRows(rowsArray[0]);

                // Filtered Values
                setValues(valuesArray);
            },
        });

    }
    // State to store parsed data
    const [parsedData, setParsedData] = useState([]);

    //State to store table Column name
    const [tableRows, setTableRows] = useState([]);

    //State to store the values
    const [values, setValues] = useState([]);

    // state to store the assignment target
    const [assignment, setAssignment] = useState('All')

    // on page reload
    useEffect(() => {
        init();
    }, [])
    

    // runs on asn change
    useEffect(() => {
        setAssignment(asn);
        handleAssignment();
    }, [asn]);

    

    const handleAssignment = () => {
        switch(assignment) {

            case "One":
                
                break;
            case "Two":
                break;
            case "Three":
                break;
            default:

                break;

        }
    }

    return (
        <div>
            {assignment}



        </div>
        );
}

export default GraphHandler;