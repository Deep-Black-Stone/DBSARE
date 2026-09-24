# DBSARE — ملخص عربي

DBSARE هو نظام دفاع سيبراني يعتمد على الذكاء الاصطناعي، وليس مجرد LLM مربوط بأدوات أمنية.

## الفكرة
Observe -> Understand -> Collect Evidence -> Normalize -> Correlate -> Analyze -> Reason -> Investigate -> Recommend -> Execute Authorized Actions -> Verify -> Learn/Retain Knowledge -> Report.

## Brain و Memory
Brain يمثل حالة البيئة السيبرانية والعلاقات بين Hosts وServices وPorts وEvents وVulnerabilities وEvidence. Memory يحتفظ بالسياق والمعرفة وحالة البيئة وتاريخ التحقيقات.

## Evidence
مخرجات الأدوات تمر عبر Collector وParser وNormalizer ثم Evidence Store وCorrelation Engine قبل reasoning.

## Security
الأفعال الحساسة تمر عبر Policy وPermission وApproval عند الحاجة، ثم Execution وVerification وAudit.

## Phase 0
المرحلة الحالية توثيق وتصميم معماري. المكونات غير المنفذة لا يجب اعتبارها implemented.
