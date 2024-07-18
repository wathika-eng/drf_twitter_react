import { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from 'react-router-dom';
const AdvocatePage = () => {
    const params = useParams();
    const username = params.username;

    const [advocate, setAdvocate] = useState([]);
    useEffect(() => {
        getData();
    }, []
    );
    const getData = async () => {
        try {
            const response = await axios.get(`/advocates/${username}/`); // check why without / no data is returned
            setAdvocate(response.data);
        } catch (error) {
            console.error("Error fetching data:", error.message);
        }
    };
    console.log(advocate);
    return (
        <div>
            <h1 className="text-center">{advocate.bio}</h1>
            
        </div>
    );
};

export default AdvocatePage;