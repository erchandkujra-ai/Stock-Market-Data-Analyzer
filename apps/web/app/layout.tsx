import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Stock Market Data Analyzer",
  description: "Real-time stock market analysis, technical indicators and strategy backtesting.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
