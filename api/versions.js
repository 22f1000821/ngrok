export default function handler(req, res) {
  // --- CORS ---
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET,OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type, X-User-Email");

  // Handle preflight
  if (req.method === "OPTIONS") {
    return res.status(204).end();
  }

  // --- Echo X-User-Email back ---
  const userEmail = req.headers["x-user-email"];
  if (userEmail) {
    res.setHeader("X-User-Email", userEmail);
  }

  // --- Response ---
  return res.status(200).json({ version: "0.16.3" });
}
