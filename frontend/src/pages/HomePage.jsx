import { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

const HomePage = () => {
    const [advocate, setAdvocate] = useState([]);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get("/advocates/");
                setAdvocate(response.data);
                setLoading(false);
            } catch (error) {
                console.error("Error fetching data:", error.message);
                setError(error.message);
                setLoading(false);
            }
        };
        fetchData();
    }, []);

    console.log(advocate);

    return (
        <div>
            <h1 className="text-center text-2xl">Advocates</h1>
            {loading ? (
                <div>Loading...</div>
            ) : error ? (
                <div><b className="font-extrabold">Error:</b> {error}</div>
            ) : (
                <ul>
                    {advocate?.map((adv, index) => (
                        <li key={index} className="flex items-center space-x-2 mb-9 ml-7">
                            <img className="rounded-badge" src={adv.profile_pic} alt={adv.username} />
                            <Link className="font-extrabold  hover:text-white hover:cursor-pointer " to={`/advocate/${adv.username}`}>
                                {adv.username}
                            </Link>
                        </li>
                    ))}
                </ul>

            )}
        </div>
    );
};

export default HomePage;
