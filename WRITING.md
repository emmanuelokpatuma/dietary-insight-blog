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

    ## x
    (For X/Twitter. Under 260 characters including the URL (a link counts as 23 characters on X). Hook fact + one short tip + URL with utm_source=x on its own line, then 1–2 hashtags. No thread.)

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

    ## community_answer
    (For Reddit/Quora. First line: "Where: " + 2 relevant places, e.g. r/diabetes_t2, r/prediabetes, or a Quora question phrased the way people ask it. Then a genuinely helpful 120–220 word answer in plain first-person-plural or neutral voice that fully answers the question on its own, using only facts from the article. End with one optional line: "I wrote a longer guide with the sources here: <URL with utm_source=reddit&utm_medium=community>". Never mention the app. Emmanuel posts these himself and must check each community's self-promotion rules first.)

- Never invent personal experiences or anecdotes for Emmanuel. Only use the facts he has stated: he built Dietary Insight because he lives with diabetes and high blood pressure.
- When describing Emmanuel himself, always say "I live with diabetes and high blood pressure" (or "he lives with diabetes..."), never "type 2 diabetes". General educational content about type 2 diabetes as a topic is fine.

## App store links in every social post (Emmanuel, 10 Nov 2026)
Every social section (facebook, threads, x, instagram, linkedin, pinterest_description) must include BOTH Dietary Insight Cam store links, exactly as below. The App Store link has no country code (never use /us/, /gb/ etc.):

    🍎 App Store: https://apps.apple.com/app/dietary-insight-cam/id6814602853
    🤖 Google Play: https://play.google.com/store/apps/details?id=com.emergent.dietaryinsightcam.wtjahd

Placement:
- facebook: after "Read the full guide:" and the blog link, add a line "See what's on your plate with Dietary Insight Cam:" then the two store-link lines (the blog link stays first so it keeps the link preview), then the hashtags.
- instagram: right after the app mention line, before the hashtags. (These are the only URLs allowed on Instagram.)
- linkedin: at the end of the post text (the blog link still goes only in linkedin_comment).
- threads: after the blog link. The whole text must stay under 500 characters; shorten the wording if needed.
- pinterest_description: inline "App Store: <link> Google Play: <link>" after the blog link. The whole description must stay under 500 characters; shorten if needed.
- x: blog link plus both store links; shorten the wording to fit.
- community_answer: no store links (never mention the app there).
Count lengths with python before saving.
