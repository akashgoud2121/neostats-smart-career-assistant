def build_system_prompt(response_mode="Concise", rag_context="", web_context=""):
    """Build system prompt based on response mode and optional RAG/web context."""
    try:
        base_prompt = (
            "You are NeoStats Smart Career Assistant. "
            "Help users with interview preparation, resume advice, job search strategies, "
            "career planning, and professional communication. "
            "Give practical, relevant, and clear advice. "
            "Do not restate the user's question. "
            "Do not repeat points. "
            "Prefer actionable advice over theory."
        )

        if response_mode == "Concise":
            mode_instruction = (
                "Reply in one short paragraph only. "
                "Maximum 5 short sentences. "
                "No headings. "
                "No long lists. "
                "No repetition."
            )
        else:
            mode_instruction = (
                "Reply in a detailed, practical, and structured way. "
                "Use short headings where useful. "
                "Focus on the most important steps first. "
                "Give realistic preparation advice. "
                "Do not add unnecessary resources unless helpful. "
                "Avoid repetition."
            )

        context_instruction = ""
        if rag_context.strip():
            context_instruction += (
                "\nUse this retrieved document context when relevant:\n"
                f"{rag_context}\n"
            )

        if web_context.strip():
            context_instruction += (
                "\nUse this live web search context when relevant:\n"
                f"{web_context}\n"
            )

        return f"{base_prompt}\n\n{mode_instruction}\n\n{context_instruction}"

    except Exception as e:
        raise RuntimeError(f"Failed to build system prompt: {str(e)}")