from enum import Enum


class ColType(str, Enum):
    MONETARY_COP = "monetary_cop"
    MONETARY_USD = "monetary_usd"
    PERSON = "person"
    COMPANY = "company"
    PROJECT_NAME = "project_name"
    PROJECT_CODE = "project_code"
    OPP_FOLIO = "opp_folio"
    DEPT = "dept"
    TEXT_DESC = "text_desc"
    PASSTHROUGH = "passthrough"


COLUMN_TYPE_MAP: dict[str, ColType] = {
    # ── MONETARY COP ──────────────────────────────────────────────────────────
    "annual_revenue_target":                ColType.MONETARY_COP,
    "revenue_ytd":                          ColType.MONETARY_COP,
    "project_cost_ytd":                     ColType.MONETARY_COP,
    "billing_ytd":                          ColType.MONETARY_COP,
    "gross_margin":                         ColType.MONETARY_COP,
    "project_mod_cost_ytd":                 ColType.MONETARY_COP,
    "project_non_mod_cost_ytd":             ColType.MONETARY_COP,
    "direct_payroll_ytd":                   ColType.MONETARY_COP,
    "unabsorbed_direct_payroll_ytd":        ColType.MONETARY_COP,
    "expected_revenue_ytd":                 ColType.MONETARY_COP,
    "indirect_payroll_ytd":                 ColType.MONETARY_COP,
    "opex_ytd":                             ColType.MONETARY_COP,
    "financial_margin_ytd":                 ColType.MONETARY_COP,
    "planned_revenue":                      ColType.MONETARY_COP,
    "actual_revenue":                       ColType.MONETARY_COP,
    "actual_billing":                       ColType.MONETARY_COP,
    "project_inventory":                    ColType.MONETARY_COP,
    "actual_collections":                   ColType.MONETARY_COP,
    "remaining_cost_backlog":               ColType.MONETARY_COP,
    "remaining_revenue_backlog":            ColType.MONETARY_COP,
    "remaining_billing_backlog":            ColType.MONETARY_COP,
    "planned_mod_cost":                     ColType.MONETARY_COP,
    "historical_mod_cost_before_current_year": ColType.MONETARY_COP,
    "current_year_mod_cost":                ColType.MONETARY_COP,
    "total_mod_cost":                       ColType.MONETARY_COP,
    "mod_cost_variance":                    ColType.MONETARY_COP,
    "expense_amount":                       ColType.MONETARY_COP,
    "payroll_amount":                       ColType.MONETARY_COP,
    "period_mod_cost":                      ColType.MONETARY_COP,
    "accumulated_mod_cost":                 ColType.MONETARY_COP,
    "mod_available":                        ColType.MONETARY_COP,

    # ── MONETARY USD ──────────────────────────────────────────────────────────
    "annual_target":                        ColType.MONETARY_USD,
    "annual_target_margen":                 ColType.MONETARY_USD,
    "signed_contracts_ytd":                 ColType.MONETARY_USD,
    "signed_contracts_margen_ytd":          ColType.MONETARY_USD,
    "expected_ytd":                         ColType.MONETARY_USD,
    "pending_legalization":                 ColType.MONETARY_USD,
    "pending_legalization_margen":          ColType.MONETARY_USD,
    "pipeline_amount":                      ColType.MONETARY_USD,
    "pipeline_margin":                      ColType.MONETARY_USD,
    "projected_contracts_closing":          ColType.MONETARY_USD,
    "projected_margin_closing":             ColType.MONETARY_USD,
    "period_margin_target":                 ColType.MONETARY_USD,
    "period_margin_actual":                 ColType.MONETARY_USD,
    "annual_margin_target":                 ColType.MONETARY_USD,
    "annual_margin_actual":                 ColType.MONETARY_USD,
    "period_margin_gap":                    ColType.MONETARY_USD,
    "annual_margin_gap":                    ColType.MONETARY_USD,
    "pending_legalization_amount":          ColType.MONETARY_USD,
    "pending_legalization_margin":          ColType.MONETARY_USD,
    "weighted_pipeline_amount":             ColType.MONETARY_USD,
    "weighted_pipeline_margin":             ColType.MONETARY_USD,

    # ── PERSON ────────────────────────────────────────────────────────────────
    "account_manager":                      ColType.PERSON,
    "project_manager":                      ColType.PERSON,

    # ── COMPANY ───────────────────────────────────────────────────────────────
    "customer_name":                        ColType.COMPANY,

    # ── PROJECT NAME ──────────────────────────────────────────────────────────
    "project_name":                         ColType.PROJECT_NAME,
    "opportunity_name":                     ColType.PROJECT_NAME,

    # ── PROJECT CODE ──────────────────────────────────────────────────────────
    "project_pep":                          ColType.PROJECT_CODE,

    # ── OPPORTUNITY FOLIO ─────────────────────────────────────────────────────
    "opportunity_folio":                    ColType.OPP_FOLIO,

    # ── DEPARTMENT ────────────────────────────────────────────────────────────
    "business_area":                        ColType.DEPT,

    # ── TEXT DESCRIPTIONS ─────────────────────────────────────────────────────
    "expense_description":                  ColType.TEXT_DESC,
    "position_description":                 ColType.TEXT_DESC,

    # ── DATES ─────────────────────────────────────────────────────────────────
    "commercial_win_date":                  ColType.PASSTHROUGH,
    "projected_close_date":                 ColType.PASSTHROUGH,

    # ── PASSTHROUGH ───────────────────────────────────────────────────────────
    "year":                                 ColType.PASSTHROUGH,
    "month":                                ColType.PASSTHROUGH,
    "period":                               ColType.PASSTHROUGH,
    "project_type":                         ColType.PASSTHROUGH,
    "project_status":                       ColType.PASSTHROUGH,
    "project_profitability_status":         ColType.PASSTHROUGH,
    "mod_consumption_status":               ColType.PASSTHROUGH,
    "legalization_risk_level":              ColType.PASSTHROUGH,
    "closing_risk_level":                   ColType.PASSTHROUGH,
    "margin_performance_status":            ColType.PASSTHROUGH,
    "expense_category":                     ColType.PASSTHROUGH,
    "gross_margin_pct":                     ColType.PASSTHROUGH,
    "non_mod_pressure_pct":                 ColType.PASSTHROUGH,
    "mod_absorption_pct":                   ColType.PASSTHROUGH,
    "actual_revenue_progress_pct":          ColType.PASSTHROUGH,
    "expected_revenue_progress_pct":        ColType.PASSTHROUGH,
    "direct_payroll_pct":                   ColType.PASSTHROUGH,
    "indirect_payroll_pct":                 ColType.PASSTHROUGH,
    "financial_margin_pct":                 ColType.PASSTHROUGH,
    "actual_progress_pct":                  ColType.PASSTHROUGH,
    "expected_progress_pct_cuota":          ColType.PASSTHROUGH,
    "actual_progress_margen_pct":           ColType.PASSTHROUGH,
    "expected_progress_pct_margen":         ColType.PASSTHROUGH,
    "projected_compliance_pct":             ColType.PASSTHROUGH,
    "projected_compliance_margen_pct":      ColType.PASSTHROUGH,
    "planned_margin_pct":                   ColType.PASSTHROUGH,
    "actual_margin_pct":                    ColType.PASSTHROUGH,
    "revenue_execution_pct":                ColType.PASSTHROUGH,
    "billing_coverage_pct":                 ColType.PASSTHROUGH,
    "collection_coverage_pct":              ColType.PASSTHROUGH,
    "margin_deviation_pct":                 ColType.PASSTHROUGH,
    "mod_consumption_pct":                  ColType.PASSTHROUGH,
    "remaining_revenue_pct":                ColType.PASSTHROUGH,
    "period_margin_compliance_pct":         ColType.PASSTHROUGH,
    "annual_margin_compliance_pct":         ColType.PASSTHROUGH,
    "mod_execution_pct":                    ColType.PASSTHROUGH,
    "close_probability_pct":               ColType.PASSTHROUGH,
    "days_pending_legalization":            ColType.PASSTHROUGH,
    "days_to_close":                        ColType.PASSTHROUGH,
    "pending_legalization_contribution_pct": ColType.PASSTHROUGH,
    "pipeline_contribution_pct":            ColType.PASSTHROUGH,
}


def classify_column(col_name: str) -> ColType:
    return COLUMN_TYPE_MAP.get(col_name, ColType.PASSTHROUGH)
