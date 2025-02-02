// PageFormat.tsx
import React from "react";
import Footer from "../shared/Footer"; 

export const PageFormat = ({ mainContent }) => {
    return (
        <>
            <div className="page-format">
                <main className="main-content">
                    {mainContent}
                </main>

                <Footer />
            </div>
        </>
    );
};
