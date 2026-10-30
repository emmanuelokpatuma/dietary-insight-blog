# How to write a Dietary Insight Blog post

Read this before writing every post. Copy the front matter shape from an existing post in `content/posts/`.

## Choosing the topic
- Take the first entry with `status: todo` in `content/topics.yml`. Write the post for its `keyword` and `category`.
- File name: `content/posts/YYYY-MM-DD-short-keyword-slug.md`, using today's date (Europe/London).
- When finished, set that topic to `status: done` and add `post: <file name>`.
- If fewer than 10 topics are left as `todo`, add 20 new ones at the end: real phrases UK readers search for about diabetes, blood pressure, cholesterol, food allergies, African and Caribbean food, eating out and seasonal events. No duplicates.

## SEO rules
- `title`: 45–65 characters, the main keyword near the start, written for people ("How Much Salt a Day? A UK Guide...").
- `description`: 120–155 characters, answers the question and makes people want to click.
- `keywords`: the main keyword plus 3–5 close variations.
- Open with a 1–3 sentence direct answer that contains the main keyword (this is what Google shows in snippets).
- Use `##` headings phrased as the questions people ask. Use `###` only under a `##`.
- Include at least one table or numbered list where it helps.
- 700–1,200 words. Short paragraphs (max 3 sentences), plain English, UK spelling and units.
- 3 FAQ entries in the front matter (`faq`), each answer 1–3 sentences. Don't repeat them in the body.
- Link to 1–2 earlier posts on the blog where relevant, using their URL `/slug/`.

## Accuracy rules (health content, non-negotiable)
- Every number and health claim must come from a UK source you have opened this session: NHS, Diabetes UK, British Heart Foundation, Blood Pressure UK, Food Standards Agency, Allergy UK, Anaphylaxis UK, NICE, or the British Dietetic Association. List 2–4 of them in `sources` with their exact URLs.
- Never invent statistics, studies, quotes or testimonials.
- Never tell readers to change, stop or dose medication or insulin. Say "talk to your GP, diabetes nurse or dietitian".
- Never say a food, diet or the app treats, cures, reverses or prevents a condition. "Can help", "is linked to" and "is recommended by" are fine when a source supports them.
- For allergies, never say a food or the app makes something "safe". Tell readers to check the full label.

## The app mention
- Mention Dietary Insight once in the body, naturally, near the end, as a way to check meals without a label. The page template adds the download buttons and the disclaimer, so don't add them yourself.
- Say what the app does ("estimates", "flags", "suggests a swap"), never that it guarantees anything.

## Voice
Friendly, practical and calm, like a knowledgeable friend. No fear-mongering, no exclamation marks, no emoji.

## Social posts (write these with every article)
Create `content/social/<same file name as the post>.md` with these sections. Plain text, no markdown formatting inside the posts, no emoji walls (one or two emoji at most), UK spelling. Every post leads with one genuinely useful fact or tip from the article, not "new blog post!". Use the article URL with tracking, e.g. `https://blog.simplerlivez.com/<slug>/?utm_source=facebook&utm_medium=social` (change utm_source per network).

    ## facebook
    (60–120 words. Hook fact, 2–3 short lines of value, then "Read the full guide:" and the URL on its own line. Ends with 3 relevant hashtags.)

    ## threads
    (Under 450 characters. Hook + one tip + URL.)

    ## instagram
    (The facebook text, but replace "Read the full guide:" and the URL with "The full guide is on our blog: tap the link in our bio 👆", add one line "Not sure what's on your plate? Snap a photo with Dietary Insight to flag sugar, salt and fat and get a healthier swap.", then 8 relevant hashtags ending with #dietaryinsight. No URLs: they aren't clickable on Instagram.)

    ## linkedin
    (80–150 words, founder voice: Emmanuel built Dietary Insight because he lives with diabetes and high blood pressure. NO URL in the post text.)

    ## linkedin_comment
    (One line: "Full guide here:" + URL with utm_source=linkedin.)

    ## pinterest_title
    (Under 100 characters, keyword-led.)

    ## pinterest_description
    (Under 450 characters, keyword-rich, ends with the URL.)

- Never invent personal experiences or anecdotes for Emmanuel. Only use the facts he has stated: he built Dietary Insight because he lives with type 2 diabetes and high blood pressure.
