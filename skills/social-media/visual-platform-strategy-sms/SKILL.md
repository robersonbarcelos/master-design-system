---
name: visual-platform-strategy-sms
description: "When the user wants platform-specific tactical guidance for Instagram, TikTok, YouTube, Pinterest, or Facebook. Also use when the user mentions 'Instagram strategy,' 'TikTok strategy,' 'YouTube strategy,' 'Pinterest strategy,' 'Facebook strategy,' 'Reels algorithm,' 'For You Page,' 'FYP,' 'YouTube algorithm,' 'thumbnail strategy,' 'Shorts,' 'Instagram Explore,' 'trending audio,' 'Pinterest SEO,' 'Facebook groups,' 'visual platform,' or 'which visual platform should I focus on.' For text-first platforms (LinkedIn, Twitter/X, Threads, Bluesky), see platform-strategy-sms. For writing captions, see caption-writer-sms. For writing posts, see post-writer-sms."
metadata:
  version: 1.1.0
---

## When to Use

- User asks for **platform-specific tactical guidance** for Instagram, TikTok, YouTube, Pinterest, or Facebook
- User mentions "Instagram strategy," "TikTok strategy," "YouTube strategy," "Pinterest strategy," or "Facebook strategy"
- User asks about "Reels algorithm," "For You Page," "FYP," "YouTube algorithm," "Explore tab," or "trending audio"
- User wants to understand how a visual platform's algorithm, culture, or content format works
- User asks "which platform should I focus on" for a visually-led brand or creator
- User wants to adapt or cross-post visual content across platforms

## Role

You are an expert visual platform strategist. Your job is to give the user actionable, platform-specific tactics grounded in how each platform's algorithm, culture, and visual language actually work — not generic "post consistently and engage with your audience" advice. Every recommendation should be specific enough to act on today.

---

## Step 1 — Check for existing context

Before asking any questions, check if `.agents/social-media-context-sms.md` exists.

**If it exists:** Read the file. Note the user's platforms, goals, voice, niche, and audience. Skip any discovery questions already answered.

**If it does not exist:** Say — "I don't have your social media context yet. Run the **social-media-context-sms** skill first for the best results. Or tell me which platforms you're using, what you're trying to achieve, and what kind of content you make — and I'll give you tactical guidance right now."

---

## Step 2 — Identify the focus

Determine what the user needs:
- Tactics for a **specific platform** (deep dive)
- **Cross-posting guidance** between visual platforms
- **Platform selection** (which visual platform to prioritize)
- **Algorithm troubleshooting** (why reach is down, why views dropped, why Explore isn't triggering)
- **Format strategy** within a platform (e.g., Reels vs. carousels on Instagram)

Ask if unclear. Then deliver the relevant section(s) below.

---

## Platform Tactics

### Instagram

**Algorithm signals** (ranked by impact):
1. **Watch time / video completion rate** — the single strongest signal for Reels; Instagram measures what percentage of people watch to the end, and whether they replay
2. **Saves** — the highest-intent engagement action; saves tell the algorithm the content has lasting value, not just momentary entertainment
3. **Shares (especially to Stories)** — sharing a post to a Story exposes it to the sharer's entire audience; Instagram weighs this heavily as a distribution signal
4. **Comments** — real comments (not just emoji) signal genuine engagement; the algorithm can distinguish between low-effort and substantive replies
5. **Likes** — still matter but weighted lower than saves, shares, and comments
6. **Profile visits and follows** — a post that drives a profile visit or follow is treated as high-signal content and gets pushed further

**Content types by objective:**

| Objective | Best Format | Why |
|---|---|---|
| Growth (reach non-followers) | Reels | Reels are the primary non-follower distribution surface on Instagram |
| Authority / credibility | Carousel (swipe post) | Carousels have the highest average reach per post; saves are high for educational content |
| Conversion (DMs, link clicks) | Stories + swipe-up / link sticker | Stories reach warm audiences and allow direct CTAs; high purchase intent |
| Community / retention | Stories polls, questions, quizzes | Stories keep followers engaged without needing to reach new audiences |
| Discoverability in niche | Static photo with strong caption | Can rank in Explore and keyword search; lower competition than Reels |

**Posting frequency by account stage:**

| Stage | Reels | Carousels | Stories | Static |
|---|---|---|---|---|
| New (0–3 months) | 3–4x/week | 1–2x/week | Daily | 1x/week |
| Growing (3–12 months) | 4–5x/week | 2–3x/week | Daily | 1–2x/week |
| Established (1+ year) | 3–5x/week | 2–4x/week | Daily | 1x/week optional |

**Key specificity: Reels vs. carousels vs. static photos vs. Stories**

- **Reels** reach non-followers by default. They live or die in the first 1–3 seconds. The algorithm tests Reels with a small batch (~500–2,000 people first); if completion rate and engagement are strong in this test group, it distributes to a larger batch. Reels with captions/text overlays outperform those without — a significant portion of users watch on mute.
- **Carousels** have the highest average reach per post type on Instagram as of 2024–2025. Instagram re-shows a carousel to a user who didn't swipe past slide 1 — effectively giving it a second chance at engagement. Slide 1 must hook; slide 2 must reward; the final slide should include a CTA (save, share, follow). Educational and "before/after" carousels perform best.
- **Static photos** have declining organic reach but still perform for niche content, aesthetic accounts, and product photography. They rank well in Explore for keyword-matched searches and work well for pinned profile posts. Don't abandon static — just make it intentional.
- **Stories** reach existing followers only (unless boosted). They're not a discovery tool; they're a retention and conversion tool. Post 5–10 Stories per day for maximum retention. Use interactive stickers (poll, question, quiz, slider) at least 3x per week — they're the highest-engagement Story element.

**Explore tab vs. feed of followers:**
- **Explore** is powered by the accounts a user already follows and engages with, not hashtags. If your content gets strong engagement from your existing audience, it signals Explore that your content is worth surfacing to similar users. Explore does not respond to hashtags as a primary signal — it responds to engagement quality and topic signals from your captions, alt text, and visual content.
- **Follower feed** is relationship-based. Followers see your content ranked by their individual engagement history with your account. A follower who regularly likes or saves your posts will see you near the top of their feed. A follower who never interacts will gradually stop seeing you.

**Trending audio: when to use, when to avoid:**
- **Use trending audio when:** your content can naturally incorporate it without feeling forced, you're creating entertainment or lifestyle content where sound is part of the experience, and the audio has been trending for less than 5–7 days (early adoption gets priority distribution).
- **Avoid trending audio when:** your brand voice is professional or corporate (mismatched audio signals inauthenticity), the audio is already peaking (you'll be too late), your audience is primarily watching on mute (add captions and treat audio as secondary), or the audio is associated with a trend that conflicts with your positioning.
- **Original audio:** Accounts that consistently use original audio can build a recognizable audio identity. If multiple creators use your original audio, Instagram gives your account credit and additional distribution.

**Collaborations and co-authorship as reach amplifiers:**
- Instagram's **Collab post** feature lists two accounts as co-authors on a single post. The post appears in both accounts' grids and reaches both audiences simultaneously — effectively doubling organic reach with one piece of content.
- Best collaboration strategy: partner with accounts of similar size in adjacent niches (not direct competitors). A photography account collaborating with a travel account reaches both audiences without audience overlap.
- **Paid partnerships tag** is required for sponsored content but does not suppress reach the way it once did — Meta's algorithm has adapted.
- **Mention + tag** in Stories (tagging someone in a Story) allows them to reshare it to their own Stories. This is a low-friction amplification loop — post content that mentions or features others and make it easy for them to reshare.

**Hashtag strategy:**
Hashtags on Instagram in 2024–2025 have reduced algorithmic weight compared to prior years. They now function more as indexing tags than reach amplifiers. Use **3–8 specific hashtags** rather than 30 generic ones. Prioritize mid-size hashtags (50K–500K posts) where your content has a chance to rank. Niche hashtags (#uxdesigntips, #remoteworklife) outperform broad ones (#design, #work) for qualified reach.

**Example Instagram Reels structure:**

```
[0–2 sec] Visual hook: unusual angle, bold text overlay, or unexpected moment
[2–5 sec] Setup: context that makes the viewer feel they need to keep watching
[5–20 sec] Payoff / value delivery: the tip, transformation, or story
[20–30 sec] Conclusion + CTA: "Save this for later" or "Which one are you? Comment below"

Caption (below the video):
Line 1 — mirror the hook or expand on it (before the "more" cutoff at ~125 chars)
Line 2 onwards — context, story, or deeper breakdown
End with a direct question or CTA
Hashtags on a new line or at the end
```

---

### TikTok

**Algorithm signals** (ranked by impact):
1. **Video completion rate** — the primary ranking signal; TikTok measures whether people watch to the end, and whether they replay. A 30-second video watched 3x is worth more than a 3-minute video abandoned halfway.
2. **For You Page (FYP) interactions** — likes, comments, shares, and saves all feed into the recommendation model; shares are especially powerful because they expose content to a new network
3. **Re-watches and loops** — TikTok videos loop automatically; the algorithm tracks intentional replays as a strong positive signal
4. **Comments and replies** — replies to comments by the creator extend the engagement window; TikTok rewards creator participation in their own comment section
5. **Profile visits** — a video that drives profile visits is treated as high-signal content
6. **"Not interested" signals** — when users mark content as "not interested" or skip quickly, it suppresses distribution; a high skip rate in the first 0–2 seconds kills a video's reach

**Content types by objective:**

| Objective | Best Format | Why |
|---|---|---|
| Growth (reach new audience) | FYP-optimized trending content | FYP reaches non-followers first; it's the primary discovery surface |
| Authority / credibility | Educational series, POV commentary | Repeat viewers build follower conversion over time |
| Conversion (DMs, link in bio) | CTA-driven tutorials, before/after | TikTok's link-in-bio is the standard conversion path; drive there explicitly |
| Community / retention | Duets, stitches, Q&A responses | Interactive formats build parasocial loyalty and comment engagement |
| Entertainment / virality | Trend participation, reaction content | Trend participation gets boosted if done within 24–48 hours of trend peak |

**Posting frequency by account stage:**

| Stage | Videos/week | Notes |
|---|---|---|
| New (0–3 months) | 5–7x/week | Test heavily; find what formats resonate; quantity matters for signal data |
| Growing (3–12 months) | 4–6x/week | Reduce quantity slightly; improve quality based on what worked |
| Established (1+ year) | 3–5x/week | Consistency over volume; use LIVE sessions to supplement reach |

**TikTok SEO — search inside the app:**
TikTok has become a search engine, particularly for Gen Z and Millennial users. An estimated 40% of Gen Z users prefer TikTok or Instagram over Google for searches like "best coffee shops in [city]" or "how to fix [problem]." This has major implications for strategy:

- **Include your keyword in the first 3 seconds of speech** — TikTok's auto-captioning and search indexing reads spoken words
- **Add the keyword as a text overlay** — on-screen text is indexed by TikTok's search algorithm
- **Put the keyword in your caption** — caption text is searchable; write captions like search queries, not poetry
- **Use keyword-matched hashtags** — e.g., #coffeetips #howtomakecoldbrewcoffee rather than #coffee #lifestyle
- **Say the keyword multiple times** — frequency of a spoken term in a video increases its search ranking for that term
- **Optimize for "answer intent"** — TikTok search favors videos that directly answer a question; structure your content to match "how to X," "best X for Y," "why your X isn't working"

**For You Page (FYP) vs. followers as distinct destinations:**
- **FYP** is TikTok's primary content surface and the default experience for most users. Every video is tested with a small initial audience (typically users who have shown interest in similar topics); if it performs well (completion rate, engagement), it's pushed to a larger batch. FYP reach is not follower-dependent — a new account can go viral on FYP.
- **Follower feed** exists but is a secondary surface. Many TikTok users never visit the "Following" tab. This means TikTok is fundamentally different from Instagram: followers are less valuable as a direct reach mechanism and more valuable as a signal of account authority.
- **Implication for strategy:** Optimize primarily for FYP metrics (completion rate, shares, rewatches), not follower engagement. A video that performs well among non-followers is doing its job.

**Series vs. standalone content:**
- **Standalone videos** are designed to be fully self-contained and to perform on FYP without any prior context. They're better for growth and discoverability.
- **Series** (e.g., "Part 3 of my 30-day challenge") build follower loyalty and return visits, but perform less well on FYP because they require prior context. Use series strategically: create a standalone hook that works without context, then reward series followers with depth.
- **"Part 2" strategy:** Creators often deliberately end a video at a moment of tension and announce "Part 2 coming tomorrow." TikTok tracks "follow" actions that happen immediately after a video ends; if a Part 1 drives a significant follow spike, TikTok will boost the Part 2 because it has a built-in engaged audience.

**The first 1–3 seconds determine distribution:**
TikTok's algorithm measures whether a user stops scrolling to watch a video. The "scroll-stop rate" in the first 1–3 seconds is the most critical metric for distribution. If users scroll past immediately, the video is suppressed; if they stop and watch, it gets tested with a larger audience.

Hooks that work on TikTok:
- **Visual disruption:** unusual framing, unexpected movement, text appearing suddenly
- **Pattern interrupt:** start mid-sentence, mid-action, or mid-story — don't start at the beginning
- **Bold text overlay in frame one:** "I spent $10,000 on this mistake" immediately conveys stakes
- **Spoken hook as first words:** TikTok indexes the first words of your video; make them count
- **Tension/promise:** "If you're doing this one thing wrong, here's why your content isn't growing"

What kills reach in the first 3 seconds:
- Blank intro screen (even 0.5 seconds of nothing loses viewers)
- Talking head with no visual element other than a face
- Starting with "Hey guys, welcome back to my channel"
- Slow build with no payoff signal in the first 2 seconds
- Reading from notes with eyes looking down

**Specifics that don't translate to other platforms:**
- **Duet and Stitch:** Reacting to or remixing another creator's content with their video playing alongside yours. Highly effective for commentary, education, and response content. Enables organic collaboration without a formal partnership.
- **TikTok LIVE:** Live streaming feeds a separate algorithm; LIVE performance doesn't depend on follower count and can introduce you to new audiences who discovered you in a live session. LIVE sessions longer than 30 minutes outperform shorter ones.
- **Green screen effect:** A native TikTok feature that lets you use any image as a background while speaking. Extremely effective for commentary, reactions, and "breaking news" style content.

---

### YouTube

**Algorithm signals** (ranked by impact):
1. **Click-through rate (CTR)** — YouTube serves your thumbnail/title to a test audience; the percentage that clicks determines how broadly YouTube distributes the video. A 4–10% CTR is strong for most niches.
2. **Average view duration and watch percentage** — how many minutes of your video the average viewer watches. YouTube values total watch time delivered, not just the percentage, so a 20-minute video that keeps 50% attention can outrank a 5-minute video with 80% retention.
3. **Retention in the first 30 seconds** — this is treated as a separate signal from overall retention. A significant drop in viewers in the first 30 seconds signals a misleading thumbnail or poor opening, and YouTube suppresses the video. The first 30 seconds are disproportionately important.
4. **Returning viewers and subscriber satisfaction** — YouTube tracks whether your subscribers seek out your content (notification clicks, homepage clicks from subscribers). High subscriber engagement signals a healthy channel.
5. **Session starts** — videos that are often the first video a user watches in a session are considered high-intent content and are promoted in homepage recommendations.
6. **Likes and comments** — secondary signals; they confirm engagement quality but are not the primary ranking factor

**Content types by objective:**

| Objective | Best Format | Why |
|---|---|---|
| Growth (new audience) | Search-optimized how-to, tutorials | YouTube Search is the second largest search engine; search-intent content drives consistent discovery |
| Authority / credibility | Long-form documentary, case study, deep dive | Long-form signals investment and expertise; drives subscribes from converted viewers |
| Conversion | Product review, comparison, demo | High purchase-intent audience; converts to link clicks and affiliate revenue |
| Community / retention | Vlogs, series, behind-the-scenes | Builds parasocial connection; subscribers return for personality, not just information |
| Viral / social sharing | Shorts, emotional storytelling | Shorts feed into Shorts-specific algorithm; emotional content gets cross-platform shares |

**Posting frequency by channel stage:**

| Stage | Long-form | Shorts |
|---|---|---|
| New (0–3 months) | 1x/week (consistent) | 3–5x/week (optional, for discovery) |
| Growing (3–12 months) | 1–2x/week | 3–7x/week if Shorts strategy is active |
| Established (1+ year) | 1–2x/week (quality over volume) | Supplemental — tied to long-form pipeline |

**Thumbnail + title as an inseparable pair:**
This is the most important and most misunderstood element of YouTube strategy. YouTube's algorithm serves the thumbnail/title combination to users; it cannot be evaluated as separate components. The thumbnail gets the initial attention; the title closes the decision to click.

Rules for the pair:
- **The thumbnail creates curiosity; the title resolves it — partially.** Never show everything in both. If the thumbnail shows a shocked face holding a product, the title should explain the stakes, not repeat the visual.
- **Do not optimize the thumbnail without reading the title next to it.** Test them together. A stunning thumbnail with a weak title will underperform.
- **Text on thumbnails should be 3–5 words maximum** — enough to add context but readable at 120px wide (mobile thumbnail size).
- **High-contrast, clean thumbnails outperform cluttered ones.** YouTube's own research shows that clear focal point + high contrast + visible face (with emotion) consistently outperforms abstract or text-only thumbnails.
- **CTR benchmarks by niche:** News/commentary: 8–12%. Tutorial/education: 5–8%. Entertainment: 6–10%. If your CTR is below 4%, fix the thumbnail/title before addressing anything else.

**Retention in the first 30 seconds:**
YouTube Analytics shows a "relative audience retention" graph for every video. The first 30 seconds almost always have the steepest drop — this is normal. What is not normal (and will suppress distribution) is a drop of more than 30–40% in the first 30 seconds.

Tactics for the first 30 seconds:
- **Open with the payoff, not the setup.** Start with the most interesting moment or a direct statement of what the viewer is about to learn. Then rewind to the context.
- **Pattern interrupt at second 5–10:** a cut, a sound effect, a visual change, or a bold statement that prevents the early bail-out
- **The "credibility bridge":** briefly establish why you're the right person to deliver this content — not a long intro, just 10–15 seconds of "I've done X, and here's what I learned"
- **No long intros.** The creator brand intro (logo animation, music) that plays before content should be eliminated or cut to under 3 seconds. Long intros are where the early dropout spike happens.

**YouTube Shorts vs. long-form:**
- **Shorts** live in a separate algorithm from long-form. Shorts subscribers do not reliably convert to long-form viewers. Shorts are a discovery and awareness tool — they can grow your subscriber count, but those subscribers may never watch your 20-minute deep dives.
- **Shorts as a funnel:** Use Shorts to introduce a topic and end with "the full breakdown is on my channel" — this can convert Shorts viewers to long-form if the content is genuinely teased, not just advertised.
- **Long-form** drives monetization, ad revenue, and deep community. It is the primary revenue-generating format. Shorts support it but do not replace it.
- **Upload separately, optimize separately:** Don't convert long-form content into Shorts by vertical-cropping — YouTube's algorithm can detect recycled content and tends to suppress it. Native Shorts (filmed vertically, edited for mobile) outperform repurposed content.

**Chapters and timestamps as retention and SEO tools:**
- **Adding chapters** (via timestamps in the video description, e.g., `0:00 Intro`, `2:30 The problem`) creates clickable chapter markers in the YouTube player. These have two major effects:
  1. **Retention:** viewers who would have abandoned the video stay longer because they can jump to the part they care about — YouTube still counts this as watch time
  2. **SEO:** YouTube indexes chapter titles as searchable text; a chapter called "How to fix slow website load time" can rank in search independently of the video title
- **Minimum 3–5 chapters** for any video longer than 10 minutes. Name chapters descriptively, not cutely ("The Big Mistake" is worse than "Why Your Thumbnails Aren't Getting Clicks").
- **End screen and cards:** Use end screens (last 20 seconds) to redirect viewers to another video or playlist. End screens drive session continuation, which is a positive YouTube algorithm signal.

**Specifics that don't translate to other platforms:**
- **YouTube Search** is the second-largest search engine in the world. Videos created around specific search queries ("how to edit videos on iPhone," "best ergonomic chair under $500") drive consistent, compounding traffic for months or years after upload.
- **Playlists as SEO:** Organize your videos into playlists. YouTube treats playlists as a ranking signal and will recommend playlist videos to users who complete one video in the sequence — an automated "watch next" system.
- **Community tab:** Available to channels with 500+ subscribers. Functions as a lightweight social feed for your existing audience — polls, images, text updates. High engagement on Community posts signals YouTube that your channel has an active subscriber base, which improves overall recommendation rates.

---

### Pinterest

**Algorithm signals** (ranked by impact):
1. **Keyword relevance** — Pinterest is a search engine first. The title, description, and board name are indexed and matched to user search queries. Keyword presence is the primary ranking factor, not engagement.
2. **Save rate (Repins)** — when users save a pin to their own boards, it signals relevance and quality. Saves extend the pin's distribution over time — each save is a new placement on a new board.
3. **Click-through rate** — pins with high CTR (clicks to destination URL) are surfaced more in search results and the home feed. A pin that drives traffic is a pin that Pinterest rewards.
4. **Pin quality and completeness** — complete pins (with title, description, alt text, and destination URL) rank higher than incomplete ones. Pinterest's algorithm penalizes spam-like or incomplete content.
5. **Board quality** — boards with consistent themes, keyword-rich descriptions, and high save rates raise the ranking of all pins within them. An authoritative board elevates the pins inside it.
6. **Account authority** — older accounts with consistent activity and good engagement history rank higher than new accounts, even for identical content.

**Content types by objective:**

| Objective | Best Format | Why |
|---|---|---|
| Traffic generation | Static pin with strong CTA image | Drives click-throughs to blog posts, product pages, or landing pages |
| Brand awareness | Idea Pin (multi-page) | Immersive, stays on Pinterest; builds brand recognition without needing clicks |
| Product sales | Product pin (shopping pin) | Connects to e-commerce catalog; shows price and availability inline |
| Education / authority | Infographic pin, step-by-step | High save rate for reference content; drives long-tail search discovery |
| Content amplification | Pin linked to YouTube/blog | Pinterest can drive significant external traffic to long-form content |

**Posting frequency by account stage:**

| Stage | Pins/day | Notes |
|---|---|---|
| New (0–3 months) | 5–10/day | Mix of original pins and curated repins; build board authority quickly |
| Growing (3–12 months) | 10–15/day | Increase original content ratio; schedule with Tailwind or Pinterest scheduler |
| Established (1+ year) | 5–25/day | Volume matters; Pinterest rewards consistent, high-frequency pinning |

**Pinterest as a search engine, not a social network:**
This is the most important reframe for Pinterest strategy. Pinterest does not function like Instagram or TikTok. There is no "For You Page" driven by viral mechanics. There is no engagement loop driven by comments or likes. Pinterest is a discovery-and-inspiration search engine where users search for ideas, save content to boards, and return to those boards when they're ready to act.

Implications:
- **The goal is to be found in search, not to go viral.** Optimize every pin for the keywords users are actively searching.
- **Traffic compounds over time.** A well-optimized pin can drive traffic for 12–24 months after it's published — unlike Instagram Reels or TikTok videos that peak in 24–72 hours and then decay.
- **Engagement numbers are less important than search rank.** A pin with 50 repins and strong keyword match will consistently outperform a pin with 500 likes and weak keyword optimization.

**Pin lifespan vs. other platforms:**
| Platform | Average Content Lifespan |
|---|---|
| Instagram (feed post) | 24–48 hours |
| TikTok | 1–7 days (can resurface for weeks in rare cases) |
| YouTube (long-form) | Weeks to months (search-indexed) |
| Pinterest (static pin) | 3 months to 3+ years |
| Pinterest (Idea Pin) | Permanent (no link, lives on platform) |

This long lifespan means Pinterest is a compounding traffic asset. The investment of creating high-quality, keyword-optimized pins pays dividends for years, unlike most social media content.

**Idea Pins vs. Static Pins vs. Video Pins:**
- **Static Pins** are the workhorses of Pinterest traffic. A vertical image (2:3 ratio, 1000x1500px recommended) with a keyword-rich title and description, linked to a destination URL. Highest click-through potential. Best for blog posts, product pages, and lead magnets.
- **Idea Pins** (formerly Story Pins) are multi-page, immersive pins that stay on Pinterest — they do not drive external traffic. They build brand awareness and save rates. Pinterest gives Idea Pins priority distribution in the home feed. Use them to build brand presence and save rates; use static pins to drive traffic.
- **Video Pins** autoplay in the feed and drive higher engagement rates than static pins. They can be linked to an external URL. Best for tutorials, product demos, and before/after content. Video Pins with text overlays perform better because Pinterest users often scroll silently.

**Keywords in title and description:**
- **Title:** 100 characters maximum. Put the primary keyword as close to the beginning as possible. Write the title as a phrase users would actually search: "Minimalist living room ideas for small apartments" not "Our favorite cozy interior moments."
- **Description:** 500 characters maximum (only the first ~50 are visible before "read more"). Pack the primary keyword, 2–3 secondary keywords, and a natural sentence structure. Do not keyword-stuff (Pinterest can penalize this). Write for a human who found the pin in search and wants to know if it's worth clicking.
- **Board name:** The board a pin lives on affects its search ranking. Name boards with primary keywords, not cute or branded names. "Content Marketing Tips" outranks "My Marketing Musings" for search placement.
- **Alt text:** Pinterest indexes alt text. Write descriptive, keyword-rich alt text for every pin.

**Specifics that don't translate to other platforms:**
- **Pinterest Trends tool:** Pinterest offers a free trends tool that shows the search volume trajectory for keywords. Use it to find keywords that are trending upward and create content around them 2–4 weeks before peak search season (e.g., "Valentine's Day gift ideas" peaks in late January — pin in December).
- **Seasonal content has a long lead time.** Pinterest users plan ahead. Back-to-school content peaks 6–8 weeks before school starts. Holiday content peaks 4–8 weeks before the holiday. Create seasonal content significantly earlier than you would for other platforms.
- **Group boards** (collaborative boards where multiple creators pin to the same board) were powerful for reach amplification historically. Their algorithmic influence has declined, but they still provide distribution to audiences of all board contributors.

---

### Facebook

**Algorithm signals** (ranked by impact):
1. **Meaningful social interactions** — Facebook's algorithm heavily prioritizes content that generates comments and discussion, especially replies within comment threads. A post with 20 engaged comments outperforms a post with 200 likes.
2. **Video watch time** — Facebook rewards native video with extended watch time, particularly videos watched to the 1-minute mark and beyond. Reels on Facebook get separate algorithmic treatment (see below).
3. **Shares** — sharing a post, especially with added commentary ("This is exactly what I was talking about"), is the highest-reach action on Facebook. Shares extend content to networks outside your direct followers.
4. **Post type preferences** — Facebook's algorithm knows each user's preferred content type (video, photo, link, text) and serves them more of it. This makes consistency in format more important on Facebook than on most platforms.
5. **Reactions** — all reactions (love, care, haha, wow, sad, angry) are weighted higher than a basic "like." Posts that generate emotional reactions beyond a thumbs-up are boosted.
6. **Early engagement velocity** — the first 30–60 minutes after posting determine the initial distribution pool. Posts that get rapid early engagement are pushed to a broader audience.

**Content types by objective:**

| Objective | Best Format | Why |
|---|---|---|
| Growth (non-follower reach) | Facebook Reels | Reels reach non-followers; highest organic reach of any Facebook format |
| Community / engagement | Facebook Groups post or poll | Groups have far higher organic reach than Pages; community content drives discussion |
| Authority / brand | Native video (3–10 min) | Long-form native video is prioritized over link posts; establishes expertise |
| Conversion | Link post to landing page | Still the primary conversion mechanism; pair with retargeting ads for best results |
| Retention / loyalty | Stories | Stories reach warm audiences; interactive stickers drive engagement signals |

**Posting frequency by account stage:**

| Stage | Page posts/week | Group posts/week |
|---|---|---|
| New (0–3 months) | 3–5x/week | 5–7x/week |
| Growing (3–12 months) | 3–5x/week | Daily or near-daily |
| Established (1+ year) | 3–7x/week | Daily + community moderation |

**Organic reach: Pages vs. personal profiles vs. Groups:**
This is the most important structural reality of Facebook strategy, and most creators and businesses get it wrong:

- **Pages:** Organic reach for Facebook Pages is effectively 1–6% of the Page's followers, depending on the niche and content type. This has declined steadily since 2012. A Page with 10,000 followers might reach 200–600 people organically per post. Pages are primarily useful as an advertising base (for running paid ads) and as a credibility signal.
- **Personal profiles:** Posts from personal profiles consistently reach 10–20%+ of friends, and can reach far beyond through shares. Facebook's algorithm was built for personal connections. If the business allows it, posting from a personal profile and linking to the business is often more effective than posting from the Page directly.
- **Groups:** Facebook Groups are the highest organic-reach surface on Facebook as of 2024–2025. Group posts regularly reach 20–50%+ of members, and active members receive notifications for new posts. Groups are where Facebook's "meaningful social interactions" metric is most naturally generated.

**Facebook Groups as a community growth strategy:**
- **Create your own Group** around a topic related to your expertise, not your brand. A personal finance brand that creates "Debt-Free Living Community" will grow faster than one that creates "Brand X Official Community" — the topic-first framing attracts members who want the conversation, not the brand.
- **Moderate actively.** Facebook's algorithm punishes Groups with low moderation quality (spam, low-effort posts). Active moderation of quality and removal of spam directly improves Group reach.
- **Post types that drive Group engagement:** polls ("Which of these mistakes have you made?"), questions ("What's your biggest challenge with X?"), wins/results posts that trigger celebratory reactions, and resource shares that prompt saves and comments.
- **Admin-only posts vs. open posts:** Consider whether to allow all members to post. Open posting drives more content volume but requires heavier moderation. Admin-only posting maintains quality but slows community feeling. A hybrid — members can post but all posts require approval — balances both.

**Facebook Reels as a reach amplifier for non-followers:**
Facebook Reels, introduced as Meta's response to TikTok, have the highest organic non-follower reach of any content type on Facebook. Key differences from Instagram Reels:
- Facebook Reels reach an older demographic (the average Facebook user is 30–50; Instagram skews 18–34)
- Facebook Reels can be posted directly to the Page and will reach non-followers through the Reels tab and home feed
- Cross-posting Instagram Reels to Facebook is supported natively but may reduce distribution if the content clearly has Instagram branding (watermarks, Instagram-style captions)
- Facebook Reels perform best at 15–30 seconds; longer Reels (60–90 seconds) underperform compared to Instagram

**When Facebook still makes strategic sense:**
Facebook's overall growth has plateaued in younger demographics (18–24), but remains dominant in specific contexts:

- **Audience age 35+:** Facebook reaches more people over 35 than any other social platform in the US. If your product or service targets this demographic, Facebook remains essential.
- **Local businesses:** Facebook's local business tools, reviews, events, and groups ecosystem makes it uniquely effective for businesses with a physical location or local community.
- **Community-based brands:** Any brand where community, discussion, and ongoing relationship matter (fitness programs, online courses, professional networks) benefits from Groups.
- **B2C e-commerce with retargeting:** Facebook's advertising infrastructure (Meta Ads) remains one of the highest-ROI digital advertising channels, even as organic reach declines. Facebook as an ad platform is distinct from Facebook as an organic content platform.
- **Event-based content:** Facebook Events still drive real attendance and have strong notification/reminder systems. For webinars, launches, and live events, Facebook Events outperform most alternative channels for organic reach.

---

## Visual Platform Selection Framework

### Decision matrix: Objective → Best Visual Platform

| Primary Goal | Best Platform | Secondary Platform | Avoid If |
|---|---|---|---|
| Short-form video growth | TikTok | Instagram (Reels) | Your audience is 45+ |
| Long-form video / authority | YouTube | Facebook (native video) | You're unwilling to invest in editing |
| Visual brand / aesthetics | Instagram | Pinterest | Your content is not visually-led |
| Product discovery / shopping | Pinterest | Instagram | Your product requires demo video |
| Community building | Facebook Groups | Instagram (Stories) | You need young audience |
| Search-driven traffic | YouTube | Pinterest | You need fast results (both are slow to compound) |
| Local / event-based | Facebook | Instagram | You're targeting a global audience |
| Viral reach / entertainment | TikTok | Instagram (Reels) | Your brand voice is formal or corporate |

### Platform prioritization by audience age

| Age group | Primary recommendation | Why |
|---|---|---|
| 13–24 | TikTok, then YouTube | Highest TikTok penetration; YouTube for education |
| 25–34 | Instagram, then TikTok | Mixed-platform; Instagram is still dominant |
| 35–44 | Instagram, then Facebook | Facebook begins to regain relevance |
| 45–54 | Facebook, then YouTube | Facebook dominant; YouTube strong for how-to |
| 55+ | Facebook, then YouTube | Strongest age cohort on both platforms |

### When to add a visual platform vs. double down

**Add a new visual platform when:**
- You've built a consistent posting rhythm on your primary platform (posting at minimum 80% of your target schedule for 90+ days)
- You have a content format that maps naturally to the new platform (e.g., tutorial videos → YouTube)
- You can repurpose or adapt existing content to fit the new platform without starting from scratch
- Your target audience demonstrably lives on the new platform more than your current one

**Double down on existing when:**
- Engagement is growing but slowly — visual platform algorithms reward consistency and punish abandonment
- You're posting inconsistently; the algorithm penalizes gaps in publishing cadence
- You don't yet understand what performs on your current platform — adding a second platform before this means learning two unknowns simultaneously
- Adding a new platform would pull your production capacity below a sustainable threshold

**Rule of thumb:** One visual platform done at 80% consistency beats three visual platforms done at 30% consistency. Algorithms read abandonment and inconsistency as signals of low-quality accounts.

---

## Cross-Posting Between Visual Platforms

### What to adapt, what to never copy

| Content Type | Cross-Post? | Adaptation Required |
|---|---|---|
| Vertical video (Reels/TikTok) | Yes, with heavy edits | Remove platform watermarks; re-cut for platform duration; adjust caption style |
| Horizontal YouTube video | Partial — cut into Reels/TikToks | Extract the most compelling 30–60 second segments; add text overlays; re-caption |
| Static photo | Yes, minimal changes | Adjust aspect ratio (square for Instagram, 2:3 for Pinterest); rewrite caption |
| Pinterest infographic | Partial | Too much text for Instagram; works as carousel if reformatted |
| Stories | No | Stories are ephemeral and platform-specific; do not cross-post |
| Facebook Group post | No | Group content is conversational and community-specific; out of context on other platforms |

### Common cross-posting mistakes between visual platforms

- **Cross-posting TikTok videos with the TikTok watermark to Instagram Reels** — Instagram's algorithm suppresses Reels identified as recycled content from TikTok. Always download the original (no watermark) using SnapTik or the native "Save video" before the final post.
- **Using the same caption on Instagram and Pinterest** — Instagram captions are conversational and personality-driven; Pinterest descriptions are keyword-optimized for search. They need completely different treatment.
- **Posting YouTube-length content on Instagram or TikTok** — long-form YouTube content does not translate; extract the core insight and build a new short-form piece.
- **Posting at the same time on all platforms** — each platform has distinct peak hours; mass scheduling the same post at the same time to all platforms sacrifices optimal timing on most of them.
- **Applying Instagram's hashtag strategy to TikTok** — Instagram uses hashtags for indexing; TikTok uses spoken keywords, text overlays, and captions for search. Stuffing 30 hashtags on a TikTok caption provides minimal benefit.
- **Expecting the same content cadence to work across platforms** — Pinterest rewards daily pinning at volume; TikTok rewards daily video; YouTube rewards weekly quality. Running all three on an "Instagram schedule" of 4x/week will underperform on all three.

### Adaptation checklist per platform

**Before posting on Instagram:**
- [ ] Aspect ratio is correct (9:16 for Reels, 4:5 for feed, 1:1 for square)
- [ ] TikTok watermark removed if source is TikTok
- [ ] Caption is conversational, personality-driven, ends with a question
- [ ] 3–8 hashtags added (mid-size niche hashtags)
- [ ] Hook is visible in the thumbnail frame

**Before posting on TikTok:**
- [ ] First 1–3 seconds have a strong visual/verbal hook
- [ ] Primary keyword is spoken in the first 3 seconds
- [ ] Primary keyword appears as text overlay
- [ ] Caption contains keyword phrases (not just hashtags)
- [ ] Video loops cleanly (end connects to beginning for re-watch)

**Before posting on YouTube:**
- [ ] Thumbnail and title tested as a pair (read them side by side)
- [ ] Primary keyword appears in the title
- [ ] Primary keyword appears in the description within the first 100 characters
- [ ] Chapters/timestamps added for videos over 8 minutes
- [ ] End screen added pointing to the next recommended video

**Before posting on Pinterest:**
- [ ] Title contains primary keyword (closest to the front as possible)
- [ ] Description contains primary keyword + 2–3 secondary keywords
- [ ] Image is 2:3 ratio (1000x1500px)
- [ ] Destination URL is active and correct
- [ ] Pin is saved to the most relevant, keyword-named board

**Before posting on Facebook:**
- [ ] Content type matches the objective (Reel for reach, Group post for community, native video for authority)
- [ ] Instagram watermarks removed from cross-posted Reels
- [ ] Caption is adapted for Facebook's older average audience
- [ ] Link is posted in the post body (not the first comment, as on LinkedIn)
- [ ] Posted at peak Facebook engagement time (6–9 AM or 7–9 PM in the audience's timezone)

---

## Platform Quick Reference

| Platform | Primary Function | Best Format | Posting Frequency | Ideal Aspect Ratio | Content Lifespan |
|---|---|---|---|---|---|
| Instagram | Visual brand + Reels discovery | Reels, Carousels | 4–7x/week | 9:16 (Reels), 4:5 (feed) | 24–72 hours (Reels peak) |
| TikTok | Short-form video discovery | Vertical video | 5–7x/week | 9:16 | 1–7 days (can resurface) |
| YouTube | Long-form authority + search | Long-form + Shorts | 1–2x/week (LF) | 16:9 (LF), 9:16 (Shorts) | Weeks to years |
| Pinterest | Visual search engine | Static pin, Idea Pin | 5–25 pins/day | 2:3 (1000x1500px) | 3 months to 3+ years |
| Facebook | Community + local + older demographic | Groups, Reels, native video | 3–7x/week | Variable | 24–48 hours |

---

## Boundaries

This skill provides platform strategy and tactical frameworks. It does **not**:

- **Write captions or post copy** — see **caption-writer-sms** for platform-specific caption writing
- **Write post bodies or social media copy** — see **post-writer-sms** for content creation
- **Write hook lines or opening statements** — see **hook-writer-sms** for hook writing by platform
- **Write carousel slide copy** — see **carousel-writer-sms** for carousel content
- **Define overall content strategy or content pillars** — see **content-strategy-sms** for strategic planning
- **Analyze post performance or interpret metrics** — see **performance-analyzer-sms** for analytics
- **Schedule or build a content calendar** — see **content-calendar-sms** for editorial planning
- **Create images, thumbnails, or visual assets** — design tools and asset creation are outside this skill's scope
- **Cover text-first platforms** (LinkedIn, Twitter/X, Threads, Bluesky) — see **platform-strategy-sms** for those platforms
- **Write video scripts** — see **video-script-sms** for video scripting

---

## See also

**platform-strategy-sms** — companion skill covering LinkedIn, Twitter/X, Threads, and Bluesky (text-first platforms)
**social-media-context-sms** — establishes the foundational profile this skill reads from
**content-strategy-sms** — defines what to post and why across all platforms
**caption-writer-sms** — writes platform-native captions for visual platforms
**hook-writer-sms** — writes scroll-stopping hooks adapted to each platform's format and culture
**post-writer-sms** — writes full social media posts from your strategy
**carousel-writer-sms** — writes carousel content for Instagram and LinkedIn
**performance-analyzer-sms** — analyzes what's working and what isn't across platforms
**content-calendar-sms** — plans posting schedules by platform and content type
**video-script-sms** — writes scripts for YouTube, TikTok, and Reels
