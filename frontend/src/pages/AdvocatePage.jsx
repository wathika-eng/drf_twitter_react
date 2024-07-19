import { useEffect, useState } from "react";
import axios from "axios";
import { useParams, Link } from 'react-router-dom';

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
    // companyData = advocate.company.map((company, index) => {
    //     return <li key={index}>{company.name}</li>;
    // });
    // console.log(companyData);
    console.log(advocate);
    return (
        <div>
            <h1 className="text-center text-2xl">@{advocate.username}</h1>
            <img src={advocate.profile_pic} alt={advocate.username} />
            <li>Bio: {advocate.bio}</li>
            {/* <li>Location: {advocate.location}</li> */}
            <li>Company: {advocate.company?.name}</li>
            <div>
                <Link to="/" className="btn btn-error-ghost">
                    Go back
                </Link>
            </div>
        </div>
    );
};
// use ? for optional chaining in nested objects 
// without it, the code will break if the nested object is not found null
export default AdvocatePage;