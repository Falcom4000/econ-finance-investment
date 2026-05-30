#!/usr/bin/env python3
"""Generate the Markdown note structure from AGENT.md.

This creates one note per section plus a linked course index. It intentionally
creates structured writing targets rather than synthetic textbook content: the
deep lecture text should be filled chapter-by-chapter after checking the source
PDFs.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AGENT = ROOT / "AGENT.md"
NOTES = ROOT / "notes"


CHAPTER_SLUGS = {
    1: "scarcity-choice-method",
    2: "supply-demand-welfare",
    3: "income-prices-unemployment",
    4: "growth-saving-investment",
    5: "financial-system-overview",
    6: "money-payments-measurement",
    7: "interest-present-value",
    8: "interest-risk-term-structure",
    9: "stocks-expectations-efficiency",
    10: "why-financial-institutions-exist",
    11: "banking-balance-sheet",
    12: "regulation-banking-structure",
    13: "financial-crises",
    14: "central-banks-money-supply",
    15: "monetary-policy-tools",
    16: "monetary-policy-strategy",
    17: "monetary-theory-ad-as-transmission",
    18: "foreign-exchange",
    19: "international-financial-system",
    20: "money-markets",
    21: "bond-markets",
    22: "stock-markets",
    23: "mortgage-markets-securitization",
    24: "mutual-funds-etf-asset-management",
    25: "insurance-pensions",
    26: "investment-banks-brokers-pe-vc",
    27: "risk-management-derivatives",
}


@dataclass
class Section:
    number: str
    title: str


@dataclass
class Chapter:
    number: int
    title: str
    part: str
    source: str = ""
    sections: list[Section] = field(default_factory=list)

    @property
    def dir_name(self) -> str:
        return f"ch{self.number:02d}-{CHAPTER_SLUGS[self.number]}"


def parse_agent() -> list[Chapter]:
    lines = AGENT.read_text(encoding="utf-8").splitlines()
    chapters: list[Chapter] = []
    current_part = ""
    current: Chapter | None = None

    for line in lines:
        part_match = re.match(r"^## (第.+部分：.+)$", line)
        if part_match:
            current_part = part_match.group(1)
            continue

        chapter_match = re.match(r"^### 第 (\d+) 章 (.+)$", line)
        if chapter_match:
            current = Chapter(
                number=int(chapter_match.group(1)),
                title=chapter_match.group(2).strip(),
                part=current_part,
            )
            chapters.append(current)
            continue

        if current is None:
            continue

        if line.startswith("原书位置："):
            current.source = line.removeprefix("原书位置：").rstrip("。")
            continue

        section_match = re.match(r"^(\d+\.\d+) (.+?)(?:  )?$", line)
        if section_match:
            current.sections.append(
                Section(
                    number=section_match.group(1),
                    title=section_match.group(2).strip(),
                )
            )

    return chapters


def split_sources(source: str) -> tuple[str, str]:
    parts = [part.strip() for part in re.split(r"；|;", source) if part.strip()]
    if not parts:
        return "待根据 AGENT.md 确认", "无"
    primary = parts[0]
    supplement = "；".join(parts[1:]) if len(parts) > 1 else "无"
    return primary, supplement


def section_path(chapter: Chapter, section: Section) -> Path:
    chapter_number, section_number = section.number.split(".")
    return (
        NOTES
        / chapter.dir_name
        / f"{int(chapter_number):02d}.{int(section_number):02d}.md"
    )


def render_note(chapter: Chapter, section: Section) -> str:
    primary, supplement = split_sources(chapter.source)
    return f"""# {section.number} {section.title}

来源：

- 主线：{primary}
- 补充：{supplement}

## 写作提示

本文件是待写脚手架。正式写作时不要保留本提示，应按内容自然分节，写成适合零基础读者连续阅读的浓缩课本。

写作时应遵守：

- 面向没有经济学和金融学基础的读者。
- 尽全力保证详细，不设置机械字数限制。
- 先让读者理解问题从哪里来，再引入概念、解释逻辑、使用例子。
- 优先沿主线教材原有推进顺序写，不强行融合三本书为新框架。
- 关键术语首次出现时，要用通俗语言解释。
- 原书例子应放在对应逻辑位置，并说明例子想澄清什么。
- 正文避免读书报告口吻；来源已在开头标明，不要频繁写“某作者认为”“教材用某例子说明”。
- 其他教材只能补充定义、背景或同一概念的辅助解释。
- 复杂机制可以使用 Mermaid 图；分类和比较可以使用 Markdown 表格。
- 图表只用于整理教材已有逻辑，不用于发明新框架。

## 小结

待写。

## 自测问题

- 这一节要解决的核心问题是什么？
- 教材是按什么逻辑一步步解释这个问题的？
- 本节最重要的术语是什么？你能用自己的话解释吗？
- 原书例子说明了什么？
"""


def render_index(chapters: list[Chapter]) -> str:
    lines = [
        "# 金融主干框架学习笔记",
        "",
        "本目录由 `AGENT.md` 生成。每节一个 Markdown 文档，正文应按原教材逻辑深度改写。",
        "",
    ]

    current_part = ""
    for chapter in chapters:
        if chapter.part != current_part:
            current_part = chapter.part
            lines.extend([f"## {current_part}", ""])

        lines.extend([f"### 第 {chapter.number} 章 {chapter.title}", ""])
        for section in chapter.sections:
            path = section_path(chapter, section).relative_to(NOTES)
            lines.append(f"- [{section.number} {section.title}]({path.as_posix()})")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    chapters = parse_agent()
    if len(chapters) != 27:
        raise SystemExit(f"Expected 27 chapters, found {len(chapters)}")

    section_count = sum(len(chapter.sections) for chapter in chapters)
    if section_count != 168:
        raise SystemExit(f"Expected 168 sections, found {section_count}")

    NOTES.mkdir(exist_ok=True)
    (NOTES / "README.md").write_text(render_index(chapters), encoding="utf-8")

    for chapter in chapters:
        chapter_dir = NOTES / chapter.dir_name
        chapter_dir.mkdir(exist_ok=True)
        for section in chapter.sections:
            path = section_path(chapter, section)
            if not path.exists():
                path.write_text(render_note(chapter, section), encoding="utf-8")

    print(f"Generated {len(chapters)} chapters and {section_count} section notes.")


if __name__ == "__main__":
    main()
