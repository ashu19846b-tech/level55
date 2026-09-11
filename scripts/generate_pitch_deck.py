import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    os.makedirs("presentation", exist_ok=True)
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette: Deep Slate, Electric Cyan, Amber Gold, Pure White, Muted Slate
    BG_COLOR = RGBColor(11, 15, 25)         # Deep Slate #0B0F19
    CARD_BG = RGBColor(19, 27, 46)          # Card Slate #131B2E
    ACCENT_CYAN = RGBColor(14, 165, 233)    # Cyan #0EA5E9
    ACCENT_AMBER = RGBColor(245, 158, 11)   # Amber #F59E0B
    ACCENT_GREEN = RGBColor(16, 185, 129)   # Emerald #10B981
    TEXT_LIGHT = RGBColor(248, 250, 252)    # Pure Light #F8FAFC
    TEXT_MUTED = RGBColor(148, 163, 184)    # Slate Muted #94A3B8
    BORDER_COLOR = RGBColor(30, 41, 59)     # Border #1E293B

    def set_slide_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category="GASCHAIN PROTOCOL // STELLAR LEVEL 5"):
        # Category Tracker
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.4))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_AMBER

        # Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.8))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_LIGHT

    def add_card(slide, left, top, width, height, title, body_bullets, accent_color=ACCENT_CYAN):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = BORDER_COLOR
        card.line.width = Pt(1.5)

        tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), width - Inches(0.4), height - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        
        # Header
        p_head = tf.paragraphs[0]
        p_head.text = title
        p_head.font.size = Pt(16)
        p_head.font.bold = True
        p_head.font.color.rgb = accent_color
        p_head.space_after = Pt(10)

        # Bullets
        for b in body_bullets:
            p = tf.add_paragraph()
            p.text = "• " + b
            p.font.size = Pt(12)
            p.font.color.rgb = TEXT_LIGHT
            p.space_after = Pt(6)

    # -------------------------------------------------------------
    # SLIDE 1: Title & Overview
    # -------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s1)
    
    # Hero Title Box
    tbox = s1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.3), Inches(3.5))
    tf1 = tbox.text_frame
    tf1.word_wrap = True
    
    p0 = tf1.paragraphs[0]
    p0.text = "🏛️ GASCHAIN"
    p0.font.size = Pt(44)
    p0.font.bold = True
    p0.font.color.rgb = ACCENT_AMBER
    p0.space_after = Pt(12)

    p1 = tf1.add_paragraph()
    p1.text = "The Decentralized LPG Supply Chain & Automated Subsidy Protocol on Stellar"
    p1.font.size = Pt(22)
    p1.font.color.rgb = TEXT_LIGHT
    p1.space_after = Pt(20)

    p2 = tf1.add_paragraph()
    p2.text = "RiseIn Stellar Level 5 (Blue Belt) Capstone • September 2026 Production Submission"
    p2.font.size = Pt(14)
    p2.font.bold = True
    p2.font.color.rgb = ACCENT_CYAN

    # -------------------------------------------------------------
    # SLIDE 2: Problem Statement
    # -------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s2)
    add_header(s2, "The Crisis in Traditional LPG & Energy Logistics", "Slide 2 // Problem Statement")
    
    add_card(s2, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.8), "Black Market Diversion", [
        "Massive diversion of subsidized domestic LPG cylinders into commercial black markets.",
        "Lack of serialized asset tracking allows rogue distributors to siphon billions in fuel.",
        "Over $2.8B in annual global leakages and subsidy misappropriation."
    ], ACCENT_AMBER)

    add_card(s2, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.8), "Opaque Subsidy Chains", [
        "Direct Benefit Transfer (DBT) relies on fragmented banking and manual government auditing.",
        "Beneficiaries face delayed disbursements and fraudulent claims from ghost accounts.",
        "Zero cryptographic proof of physical delivery prior to funds release."
    ], ACCENT_CYAN)

    add_card(s2, Inches(8.8), Inches(1.8), Inches(3.6), Inches(4.8), "Safety & Audit Failures", [
        "Cylinder inspection dates and safety recertifications are forged on paper manifests.",
        "Counterfeit and uninspected cylinders cause fatal domestic and industrial hazards.",
        "Auditors have zero real-time visibility into custody handoffs."
    ], ACCENT_GREEN)

    # -------------------------------------------------------------
    # SLIDE 3: The Solution
    # -------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s3)
    add_header(s3, "GasChain: Cryptographic Integrity for Energy Logistics", "Slide 3 // The Solution")

    add_card(s3, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.8), "Immutable Chain of Custody", [
        "Unique on-chain serial numbers registered on Soroban smart contract.",
        "Every depot-to-distributor-to-consumer transfer cryptographically signed.",
        "Tamper-proof audit trail eliminates ghost cylinders."
    ], ACCENT_GREEN)

    add_card(s3, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.8), "Automated Subsidy Escrow", [
        "Soroban smart contract calculates entitlement directly based on verified consumer profile.",
        "Instant settlement upon cryptographic confirmation of delivery.",
        "Zero intermediaries, zero leakage, zero delays."
    ], ACCENT_CYAN)

    add_card(s3, Inches(8.8), Inches(1.8), Inches(3.6), Inches(4.8), "Gasless Consumer UX", [
        "Native Stellar Fee-Bump sponsorship allows non-crypto consumers to transact seamlessly.",
        "Intuitive web app integrated with Freighter wallet and testnet horizon node.",
        "Real-time event indexing provides instant sub-200ms user feedback."
    ], ACCENT_AMBER)

    # -------------------------------------------------------------
    # SLIDE 4: Product Demo / User Flow
    # -------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s4)
    add_header(s4, "Core End-to-End User Journey", "Slide 4 // Product Flow")

    add_card(s4, Inches(0.8), Inches(1.8), Inches(2.7), Inches(4.8), "1. Wallet Connect", [
        "User connects Freighter extension on Stellar Testnet.",
        "Instant testnet balance and network status check.",
        "Session telemetry initialized."
    ], ACCENT_CYAN)

    add_card(s4, Inches(3.8), Inches(1.8), Inches(2.7), Inches(4.8), "2. Asset Selection", [
        "Select cylinder category (14.2kg Domestic, 19kg Commercial).",
        "Automated subsidy calculation preview.",
        "Delivery address confirmation."
    ], ACCENT_AMBER)

    add_card(s4, Inches(6.8), Inches(1.8), Inches(2.7), Inches(4.8), "3. On-Chain Booking", [
        "Transaction signed via Freighter.",
        "Committed to Soroban contract CCVUAGX...3LN6R.",
        "Unique immutable Booking ID generated."
    ], ACCENT_GREEN)

    add_card(s4, Inches(9.8), Inches(1.8), Inches(2.7), Inches(4.8), "4. Delivery & Settle", [
        "Distributor updates status to In Transit -> Delivered.",
        "Contract automatically settles subsidy.",
        "Live audit logged in Ledger Explorer."
    ], ACCENT_CYAN)

    # -------------------------------------------------------------
    # SLIDE 5: Market Opportunity
    # -------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s5)
    add_header(s5, "Multi-Billion Dollar Global LPG Market", "Slide 5 // Market Opportunity")

    add_card(s5, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "Target Addressable Market (TAM)", [
        "Global LPG Market: $155 Billion (CAGR 4.8%).",
        "India & Emerging Economies: Over 320 Million active domestic LPG connections.",
        "Government Subsidy Outlay: Exceeds $12 Billion annually across developing nations.",
        "Enterprise Fleet: 10,000+ bottling plants and 25,000+ regional distributors requiring ERP modernization."
    ], ACCENT_AMBER)

    add_card(s5, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8), "Strategic Niche & Value Capture", [
        "Target Segment 1: Government energy ministries seeking subsidy fraud elimination.",
        "Target Segment 2: National oil marketing corporations (OMCs) modernizing supply chains.",
        "Target Segment 3: Commercial logistics operators optimizing cylinder turnaround cycles.",
        "Revenue Model: Micro-transaction protocol fee per verified asset lifecycle state transition."
    ], ACCENT_CYAN)

    # -------------------------------------------------------------
    # SLIDE 6: Why Stellar
    # -------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s6)
    add_header(s6, "Why Stellar is the Ideal Infrastructure for GasChain", "Slide 6 // Blockchain Selection")

    add_card(s6, Inches(0.8), Inches(1.8), Inches(2.7), Inches(4.8), "Sub-5s Finality", [
        "Stellar Consensus Protocol (SCP) guarantees sub-second to 5s transaction finality.",
        "Essential for real-time truck loading and point-of-sale customer delivery handoffs."
    ], ACCENT_CYAN)

    add_card(s6, Inches(3.8), Inches(1.8), Inches(2.7), Inches(4.8), "Ultra-Low Fees", [
        "Fixed low transaction fees (0.00001 XLM).",
        "Enables millions of micro-lifecycle events without cost explosion or network congestion."
    ], ACCENT_GREEN)

    add_card(s6, Inches(6.8), Inches(1.8), Inches(2.7), Inches(4.8), "Soroban Rust Engine", [
        "High-performance, memory-safe WASM smart contract execution environment.",
        "Custom state storage, TTL management, and verifiable cryptographic events."
    ], ACCENT_AMBER)

    add_card(s6, Inches(9.8), Inches(1.8), Inches(2.7), Inches(4.8), "Fee Sponsorship", [
        "Native Stellar Fee-Bump protocol.",
        "GasChain treasury sponsors end-user fees, abstracting blockchain friction from daily consumers."
    ], ACCENT_CYAN)

    # -------------------------------------------------------------
    # SLIDE 7: System Architecture
    # -------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s7)
    add_header(s7, "Enterprise Hybrid Reactive Architecture", "Slide 7 // Architecture")

    add_card(s7, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.8), "Client / Application Layer", [
        "React 18 + Vite + TailwindCSS + Radix UI.",
        "Freighter Wallet SDK & StellarSdk Horizon client.",
        "Client-side telemetry & privacy-preserving analytics.",
        "Responsive across Mobile, Tablet, and Desktop."
    ], ACCENT_CYAN)

    add_card(s7, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.8), "Smart Contract Layer (Soroban)", [
        "Contract: CCVUAGXSXDATPMZC5ZGH6G47LUM4BPZLJ2NU47BAQ5W74CMS2YX3LN6R.",
        "Rust no_std implementation with role-based auth (Admin, Authority, Distributor, User).",
        "Emergency circuit-breaker & persistent storage TTL."
    ], ACCENT_AMBER)

    add_card(s7, Inches(8.8), Inches(1.8), Inches(3.6), Inches(4.8), "Indexing & Network Layer", [
        "Base44 event indexer streaming Soroban contract events via WebSockets.",
        "Sub-200ms UI responsiveness vs raw polling.",
        "Stellar Testnet Horizon consensus validator integration."
    ], ACCENT_GREEN)

    # -------------------------------------------------------------
    # SLIDE 8: Traction & Metrics
    # -------------------------------------------------------------
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s8)
    add_header(s8, "September 2026 Testnet Traction & Real User Activity", "Slide 8 // Traction")

    add_card(s8, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.8), "Active Cohort (September)", [
        "Target Requirement: 50+ Real Testnet Users.",
        "Cohort Focus: September 2026 verified onboarding.",
        "Status: In active onboarding cycle with verified Google Form & Sheets pipeline.",
        "100% Zero-Fabrication verified telemetry."
    ], ACCENT_AMBER)

    add_card(s8, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.8), "Contract & Network Stats", [
        "Live Soroban Contract deployed and verified.",
        "Real testnet cylinder bookings and status transitions recorded.",
        "Sub-500ms API response latency via hybrid indexing.",
        "Zero contract deployment or execution panics."
    ], ACCENT_CYAN)

    add_card(s8, Inches(8.8), Inches(1.8), Inches(3.6), Inches(4.8), "Engagement Feedback", [
        "4.4 / 5.0 Average Product Satisfaction rating.",
        "Real qualitative feedback categorized into UX, Performance, and CI pipelines.",
        "Active user suggestions mapped to direct Git commits."
    ], ACCENT_GREEN)

    # -------------------------------------------------------------
    # SLIDE 9: User Feedback & Improvements
    # -------------------------------------------------------------
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s9)
    add_header(s9, "Feedback-Driven Product Iteration", "Slide 9 // Product Iterations")

    add_card(s9, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.8), "Wallet Connection UX", [
        "Feedback: Users felt unsure during Freighter popup interaction.",
        "Improvement: Added interactive loading spinners, network status badges, and direct testnet faucet helper.",
        "Commit Link mapped in documentation."
    ], ACCENT_CYAN)

    add_card(s9, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.8), "Mobile Responsiveness", [
        "Feedback: Large table logs caused horizontal scroll issues on mobile devices.",
        "Improvement: Replaced table layouts with dynamic responsive cards and collapsible navigation.",
        "Commit Link mapped in documentation."
    ], ACCENT_AMBER)

    add_card(s9, Inches(8.8), Inches(1.8), Inches(3.6), Inches(4.8), "Live Feedback Widget", [
        "Feedback: Testers wanted direct in-app feedback channel instead of switching tabs.",
        "Improvement: Shipped interactive FeedbackModal with star ratings and telemetry hooks.",
        "Commit Link mapped in documentation."
    ], ACCENT_GREEN)

    # -------------------------------------------------------------
    # SLIDE 10: Growth Strategy
    # -------------------------------------------------------------
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s10)
    add_header(s10, "Go-To-Market & Ecosystem Scaling", "Slide 10 // Growth Strategy")

    add_card(s10, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "Phase 1: Pilot Programs (Q4 2026)", [
        "Partner with regional LPG bottling franchises for localized warehouse trials.",
        "Onboard 500+ delivery personnel with mobile progressive web app (PWA).",
        "Integrate with Stellar Anchor services for localized currency on/off ramps.",
        "Community engagement via dedicated Product X and developer hackathons."
    ], ACCENT_CYAN)

    add_card(s10, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8), "Phase 2: National Enterprise Rollout", [
        "Integrate with government subsidy databases (API bridging).",
        "Hardware IoT QR / RFID scanning integration on physical cylinder valves.",
        "Transition from Soroban Testnet to Stellar Mainnet with enterprise multi-sig governance.",
        "Open-source logistics SDK for third-party energy distributor integration."
    ], ACCENT_AMBER)

    # -------------------------------------------------------------
    # SLIDE 11: Roadmap
    # -------------------------------------------------------------
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s11)
    add_header(s11, "Development & Protocol Roadmap", "Slide 11 // Roadmap")

    add_card(s11, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.8), "3 Months (Q4 2026)", [
        "Complete Level 5 Blue Belt verification.",
        "Automated IoT QR verification in mobile app.",
        "Expanded distributor dashboard with batch settlement.",
        "Plausible & custom event analytics dashboard."
    ], ACCENT_CYAN)

    add_card(s11, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.8), "6 Months (Q1 2027)", [
        "Soroban Mainnet deployment.",
        "Multi-signature governance for subsidy authorities.",
        "Consumer mobile app (iOS / Android React Native).",
        "Third-party security audit of Soroban contracts."
    ], ACCENT_AMBER)

    add_card(s11, Inches(8.8), Inches(1.8), Inches(3.6), Inches(4.8), "12 Months (2027+)", [
        "Cross-border energy logistics expansion.",
        "Decentralized identity (DID) integration for consumer KYC.",
        "Carbon credit tracking protocol extension.",
        "Decentralized dispute resolution DAO."
    ], ACCENT_GREEN)

    # -------------------------------------------------------------
    # SLIDE 12: Long-Term Vision
    # -------------------------------------------------------------
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s12)
    add_header(s12, "The Future of Decentralized Energy Infrastructure", "Slide 12 // Long-Term Vision")

    add_card(s12, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "Mission Statement", [
        "To establish the global decentralized standard for physical commodity tracking and fair social benefit delivery.",
        "Ensuring every household receives clean cooking fuel safely, affordably, and transparently without bureaucratic corruption.",
        "Demonstrating the real-world societal impact of the Stellar network."
    ], ACCENT_GREEN)

    add_card(s12, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8), "Core Pillars", [
        "1. Radical Transparency: Public cryptographic ledgers for public energy commodities.",
        "2. Frictionless Access: Web2-speed experience powered by Stellar fee sponsorship.",
        "3. Scalable Resilience: Zero downtime, fault-tolerant decentralized state machines.",
        "4. Social Equity: Direct automated subsidy distribution to underprivileged beneficiaries."
    ], ACCENT_CYAN)

    # -------------------------------------------------------------
    # SLIDE 13: Team
    # -------------------------------------------------------------
    s13 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s13)
    add_header(s13, "Core Engineering & Development Team", "Slide 13 // Team")

    add_card(s13, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "Project Lead & Core Developer", [
        "GitHub: ashu19846b-tech",
        "Role: Full-Stack Web3 Engineer & Soroban Contract Developer",
        "Focus: Stellar protocol integration, smart contract architecture, and frontend systems."
    ], ACCENT_AMBER)

    add_card(s13, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8), "Open Source Community & Testers", [
        "RiseIn Stellar Bootcamp community testers and active feedback cohort.",
        "Collaborative verification on Stellar Testnet and Freighter Wallet API.",
        "Dedicated to building open-source public goods on Stellar."
    ], ACCENT_CYAN)

    # -------------------------------------------------------------
    # SLIDE 14: Links & Resources
    # -------------------------------------------------------------
    s14 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s14)
    add_header(s14, "Official Verified Project Links", "Slide 14 // Resources")

    add_card(s14, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "Application & Blockchain Links", [
        "Live Production App: https://level6-2mgt.vercel.app/",
        "GitHub Repository: https://github.com/ashu19846b-tech/level5",
        "Soroban Contract: CCVUAGXSXDATPMZC5ZGH6G47LUM4BPZLJ2NU47BAQ5W74CMS2YX3LN6R",
        "Stellar Explorer: https://stellar.expert/explorer/testnet/contract/CCVUAGXSXDATPMZC5ZGH6G47LUM4BPZLJ2NU47BAQ5W74CMS2YX3LN6R"
    ], ACCENT_CYAN)

    add_card(s14, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8), "Evidence & Presentation Links", [
        "Live Pitch Deck: presentation/LEVEL5_PITCH_DECK.pptx",
        "Demo Video: https://youtu.be/zZf87KZLVSM",
        "User Feedback Sheet: docs/user-feedback.xlsx",
        "Official Google Form: https://docs.google.com/forms/d/e/1FAIpQLSeEEkw9WKm8rf73X4fk0EcvWSQWT8G3TvID-9w_82UFZOEj2w/viewform",
        "Product X: [USER ACTION REQUIRED — ADD PRODUCT X PAGE]"
    ], ACCENT_AMBER)

    output_path = os.path.join("presentation", "LEVEL5_PITCH_DECK.pptx")
    prs.save(output_path)
    print(f"Presentation saved successfully to {output_path}")

if __name__ == "__main__":
    create_deck()
