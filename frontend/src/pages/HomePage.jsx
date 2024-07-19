import { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

const HomePage = () => {
    const [advocates, setAdvocates] = useState([]);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(true);
    const [total, setTotal] = useState(0);
    const [page, setPage] = useState(1);
    const [pageSize, setPageSize] = useState(3); // Number of items per page

    const fetchData = async (page) => {
        try {
            const response = await axios.get(`/advocates/?page=${page}&page_size=${pageSize}`);
            setAdvocates(response.data.results);
            setTotal(response.data.count);
            setLoading(false);
        } catch (error) {
            console.error("Error fetching data:", error.message);
            setError(error.message);
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchData(page);
    }, [page]);

    const handlePageChange = (newPage) => {
        if (newPage > 0 && newPage <= Math.ceil(total / pageSize)) {
            setPage(newPage);
        }
    };

    return (
        <div>
            <h1 className="text-center text-2xl">{total} Advocates</h1>
            {loading ? (
                <div>Loading...</div>
            ) : error ? (
                <div><b className="font-extrabold">Error:</b> {error}</div>
            ) : (
                <>
                    <ul>
                        {advocates.map((adv, index) => (
                            <li key={index} className="flex items-center space-x-2 mb-9 ml-7">
                                <img className="rounded-badge" src={adv.profile_pic} alt={adv.username} />
                                <Link className="font-extrabold hover:text-white hover:cursor-pointer" to={`/advocate/${adv.username}`}>
                                    {adv.username}
                                </Link>
                            </li>
                        ))}
                    </ul>
                    <div className="flex justify-center space-x-2 mt-4">
                        <button
                            onClick={() => handlePageChange(page - 1)}
                            disabled={page === 1}
                            className="px-4 py-2 bg-gray-200 rounded hover:bg-gray-300"
                        >
                            Previous
                        </button>
                        <span className="self-center">{page} / {Math.ceil(total / pageSize)}</span>
                        <button
                            onClick={() => handlePageChange(page + 1)}
                            disabled={page === Math.ceil(total / pageSize)}
                            className="px-4 py-2 bg-gray-200 rounded hover:bg-gray-300"
                        >
                            Next
                        </button>
                    </div>
                </>
            )}
        </div>
    );
};

export default HomePage;
