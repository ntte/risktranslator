import json
from pathlib import Path
from src.ingest.text_loader import load_text
from src.normalize.extract_findings import extract_findings
from src.generate.briefing import generate_ciso_brief, generate_cto_brief
from src.export.markdown import write_markdown

def run(input_path: str, out_dir: str = "data/processed") -> None:
    text = load_text(input_path)
    bundle = extract_findings(text)

    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    # Save structured findings
    (out / "findings.json").write_text(
        json.dumps(bundle.model_dump(), indent=2),
        encoding="utf-8"
    )

    # Generate briefs
    ciso_md = generate_ciso_brief(bundle)
    cto_md = generate_cto_brief(bundle)

    write_markdown(str(out / "CISO_Brief.md"), ciso_md)
    write_markdown(str(out / "CTO_Brief.md"), cto_md)

    print(f"Done. Outputs in: {out.resolve()}")

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="Path to assessment text file")
    ap.add_argument("--out", default="data/processed", help="Output directory")
    args = ap.parse_args()
    run(args.input, args.out)
