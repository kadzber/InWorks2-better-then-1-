/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html", "./*.js"], // Scan all HTML and JS files in the root folder
  theme: {
    extend: {
      colors: {
        primary: "#1E40AF",
        secondary: "#64748B",
      },
      fontFamily: {
        sans: ["Inter", "sans-serif"],
      },
      spacing: {
        128: "32rem",
        144: "36rem",
      },
    },
  },
  plugins: [],
};
