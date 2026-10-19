"""Render the paper figures used on the page into static/images/ (white background, web widths).

Run after the paper figures change. Needs PyMuPDF (fitz) and the paper repository checkout.
    python src/make_images.py [--figures /path/to/2026_NeurIPS_format/Figure] [protocol.png ...]
"""
import argparse
from pathlib import Path

import fitz  # PyMuPDF

JOBS = {  # page image: (paper figure PDF, width in px)
    "overview.png": ("Fig_Overview_Cute_Comic.pdf", 2000),      # Fig. 1
    "protocol.png": ("Teaser_v12_ppt.pdf", 2000),               # Fig. 3
    "validation.png": ("Fig_Validation_Summary_camera_ready.pdf", 1800),  # Fig. 4
    "f1_heatmap.png": ("Fig2_Heatmap.pdf", 1600),               # Fig. 5
    "f2_prec1.png": ("Fig_F2_combined_a.pdf", 1100),            # Fig. 6a
    "f2_concordance.png": ("Fig_F2_combined_b.pdf", 1000),      # Fig. 6b
    "f2_scene_a.png": ("Fig_F2_qualitative_a.pdf", 1300),       # Fig. 7a
    "f2_scene_b.png": ("Fig_F2_qualitative_b.pdf", 1300),       # Fig. 7b
    "f3_demo.png": ("Fig_F3_picked_a.pdf", 1300),               # Fig. 8a
    "f3_wayformer.png": ("Fig_F3_picked_b.pdf", 1300),          # Fig. 8b
    "companion.png": ("Fig_DiscussionCombined.pdf", 1500),      # Fig. 9a
    "cross_dataset.png": ("Fig_DiscussionScatter.pdf", 800),    # Fig. 9b
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--figures", type=Path,
                    default=Path("/home/geonyeong/park_ws/UniTraj/2026_NeurIPS_format/Figure"))
    ap.add_argument("names", nargs="*", help="page images to render (default: all)")
    args = ap.parse_args()
    out = Path(__file__).resolve().parents[1] / "static/images"
    out.mkdir(parents=True, exist_ok=True)
    for name, (src, width) in JOBS.items():
        if args.names and name not in args.names:
            continue
        page = fitz.open(args.figures / src)[0]
        zoom = width / page.rect.width
        page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False).save(out / name)
        print("wrote", out / name)


if __name__ == "__main__":
    main()
