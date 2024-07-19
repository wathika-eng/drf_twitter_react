
import React from 'react';
import { Outlet } from 'react-router-dom';
import Nav from './Nav';

const Layout = () => {
    return (
        <div className='container mx-auto'>
            <Nav />
            <main>
                <Outlet />
            </main>
        </div>
    );
};

export default Layout;
