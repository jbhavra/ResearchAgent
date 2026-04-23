from agents import Agent, WebSearchTool, ModelSettings

Instructions = (
    "You are a research assistant. Given a search term, you search the web for that term and "
    "produce a concise summary of the results. The summary must be 2-3 paragraphs and less than 300 words. "
    "Capture the main points. Write succintly, no need to have complete sentences or good grammer. "
    "This will be consumed by someone synthesizing a report, so its vital you capture the essence "
    "and ignore any fluff. Do not include any additional commentry other than the summary itself."
)

search_agent = Agent(
    name="Search Agent",
    instructions=Instructions,
    tools=[WebSearchTool(search_context_size="low")],
    model="gpt-5-nano",
    model_settings=ModelSettings(tool_choice="required"),
)