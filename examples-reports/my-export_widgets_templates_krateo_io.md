# CRD Schema Documentation - widgets.templates.krateo.io API Group

> **Generated:** 2025-09-07 17:05:16
> 
> **Total CRDs:** 21
> 
> **API Groups:** 1
> 
> **Description:** Complete schema documentation for Kubernetes Custom Resource Definitions (CRDs), including property definitions, types, relationships, and visual diagrams.

---

## 📋 Table of Contents

1. [Executive Summary](#-executive-summary)
2. [API Group Documentation](#-api-group-documentation)
   - [widgets.templates.krateo.io](#widgetstemplateskrateoio) (21 CRDs)
3. [Appendices](#-appendices)
   - [CRD Index](#crd-index)
   - [Property Types Summary](#property-types-summary)
   - [Relationship Matrix](#relationship-matrix)

## 📊 Executive Summary

### Overview

This document provides comprehensive schema documentation for **21 Custom Resource Definitions** distributed across **1 API groups** in your Kubernetes cluster.

### Key Statistics

| Metric | Value |
|--------|-------|
| **Total CRDs** | 21 |
| **API Groups** | 1 |
| **Total Instances** | 0 |
| **Namespaced CRDs** | 21 (100.0%) |
| **Cluster-scoped CRDs** | 0 (0.0%) |
| **Schema Coverage** | 21/21 (100.0%) |

### Distribution Analysis

#### Largest API Groups (by CRD count)

1. **widgets.templates.krateo.io**: 21 CRDs

### Schema Analysis

**Most Complex CRDs (by property count):**

1. `BarChart` (widgets.templates.krateo.io): 5 properties
2. `Button` (widgets.templates.krateo.io): 5 properties
3. `Column` (widgets.templates.krateo.io): 5 properties


## 📁 widgets.templates.krateo.io

### Overview

**API Group:** `widgets.templates.krateo.io`  
**CRDs in Group:** 21  
**Total Instances:** 0

### CRDs in this Group

| Kind | Scope | Version | Instances | Description |
|------|-------|---------|-----------|-------------|
| `BarChart` | Namespaced | v1beta1 | 0 | *No description available* |
| `Button` | Namespaced | v1beta1 | 0 | *No description available* |
| `Column` | Namespaced | v1beta1 | 0 | *No description available* |
| `DataGrid` | Namespaced | v1beta1 | 0 | *No description available* |
| `EventList` | Namespaced | v1beta1 | 0 | *No description available* |
| `Filters` | Namespaced | v1beta1 | 0 | *No description available* |
| `FlowChart` | Namespaced | v1beta1 | 0 | *No description available* |
| `Form` | Namespaced | v1beta1 | 0 | *No description available* |
| `LineChart` | Namespaced | v1beta1 | 0 | *No description available* |
| `NavMenu` | Namespaced | v1beta1 | 0 | *No description available* |
| `NavMenuItem` | Namespaced | v1beta1 | 0 | *No description available* |
| `Page` | Namespaced | v1beta1 | 0 | *No description available* |
| `Panel` | Namespaced | v1beta1 | 0 | *No description available* |
| `Paragraph` | Namespaced | v1beta1 | 0 | *No description available* |
| `PieChart` | Namespaced | v1beta1 | 0 | *No description available* |
| `Route` | Namespaced | v1beta1 | 0 | *No description available* |
| `RoutesLoader` | Namespaced | v1beta1 | 0 | *No description available* |
| `Row` | Namespaced | v1beta1 | 0 | *No description available* |
| `TabList` | Namespaced | v1beta1 | 0 | *No description available* |
| `Table` | Namespaced | v1beta1 | 0 | *No description available* |
| `YamlViewer` | Namespaced | v1beta1 | 0 | *No description available* |

### Schema Diagram

```mermaid
classDiagram
    %% API Group: widgets.templates.krateo.io
    class widgets_templates_krateo_io_BarChart {
        +string kind: BarChart
        +string apiVersion: widgets.templates.krateo.io/v1beta1
        +string scope: Namespaced
        +object apiRef
        +string apiRef.name
        +string apiRef.namespace
        +array<object> resourcesRefs
        +array<object> resourcesRefsTemplate
        +object widgetData
        +array<object> widgetData.data
        +array<object> widgetDataTemplate
    }
    widgets_templates_krateo_io_BarChart : <<Namespaced>>
    class widgets_templates_krateo_io_Button {
        +string kind: Button
        +string apiVersion: widgets.templates.krateo.io/v1beta1
        +string scope: Namespaced
        +object apiRef
        +string apiRef.name
        +string apiRef.namespace
        +array<object> resourcesRefs
        +array<object> resourcesRefsTemplate
        +object widgetData
        +object widgetData.actions
        +string widgetData.clickActionId
        +enum[16 values] widgetData.color
        +string widgetData.icon
        +string widgetData.label
        +enum[default|circle|round] widgetData.shape
        +enum[small|middle|large] widgetData.size
        +enum[5 values] widgetData.type
        +array<object> widgetDataTemplate
    }
    widgets_templates_krateo_io_Button : <<Namespaced>>
    class widgets_templates_krateo_io_Column {
        +string kind: Column
        +string apiVersion: widgets.templates.krateo.io/v1beta1
        +string scope: Namespaced
        +object apiRef
        +string apiRef.name
        +string apiRef.namespace
        +array<object> resourcesRefs
        +array<object> resourcesRefsTemplate
        +object widgetData
        +array<object> widgetData.items
        +integer widgetData.size
        +array<object> widgetDataTemplate
    }
    widgets_templates_krateo_io_Column : <<Namespaced>>
    class widgets_templates_krateo_io_DataGrid {
        +string kind: DataGrid
        +string apiVersion: widgets.templates.krateo.io/v1beta1
        +string scope: Namespaced
        +object apiRef
        +string apiRef.name
        +string apiRef.namespace
        +array<object> resourcesRefs
        +array<object> resourcesRefsTemplate
        +object widgetData
        +boolean widgetData.asGrid
        +object widgetData.grid
        +array<object> widgetData.items
        +string widgetData.prefix
        +array<object> widgetDataTemplate
    }
    widgets_templates_krateo_io_DataGrid : <<Namespaced>>
    class widgets_templates_krateo_io_EventList {
        +string kind: EventList
        +string apiVersion: widgets.templates.krateo.io/v1beta1
        +string scope: Namespaced
        +object apiRef
        +string apiRef.name
        +string apiRef.namespace
        +array<object> resourcesRefs
        +array<object> resourcesRefsTemplate
        +object widgetData
        +array<object> widgetData.events
        +string widgetData.sseEndpoint
        +string widgetData.sseTopic
        +array<object> widgetDataTemplate
    }
    widgets_templates_krateo_io_EventList : <<Namespaced>>
    class widgets_templates_krateo_io_Filters {
        +string kind: Filters
        +string apiVersion: widgets.templates.krateo.io/v1beta1
        +string scope: Namespaced
        +object apiRef
        +string apiRef.name
        +string apiRef.namespace
        +array<object> resourcesRefs
        +array<object> resourcesRefsTemplate
        +object widgetData
        +array<object> widgetData.fields
        +string widgetData.prefix
        +array<object> widgetDataTemplate
    }
    widgets_templates_krateo_io_Filters : <<Namespaced>>
    class widgets_templates_krateo_io_FlowChart {
        +string kind: FlowChart
        +string apiVersion: widgets.templates.krateo.io/v1beta1
        +string scope: Namespaced
        +object apiRef
        +string apiRef.name
        +string apiRef.namespace
        +array<object> resourcesRefs
        +array<object> resourcesRefsTemplate
        +object widgetData
        +array<object> widgetData.data
        +array<object> widgetDataTemplate
    }
    widgets_templates_krateo_io_FlowChart : <<Namespaced>>
    class widgets_templates_krateo_io_Form {
        +string kind: Form
        +string apiVersion: widgets.templates.krateo.io/v1beta1
        +string scope: Namespaced
        +object apiRef
        +string apiRef.name
        +string apiRef.namespace
        +array<object> resourcesRefs
        +array<object> resourcesRefsTemplate
        +object widgetData
        +object widgetData.actions
        +enum[tooltip|inline] widgetData.fieldDescription
        +object widgetData.schema
        +string widgetData.stringSchema
        +string widgetData.submitActionId
        +array<object> widgetDataTemplate
    }
    widgets_templates_krateo_io_Form : <<Namespaced>>
    class widgets_templates_krateo_io_LineChart {
        +string kind: LineChart
        +string apiVersion: widgets.templates.krateo.io/v1beta1
        +string scope: Namespaced
        +object apiRef
        +string apiRef.name
        +string apiRef.namespace
        +array<object> resourcesRefs
        +array<object> resourcesRefsTemplate
        +object widgetData
        +array<object> widgetData.lines
        +string widgetData.prefix
        +string widgetData.xAxisName
        +string widgetData.yAxisName
        +array<object> widgetDataTemplate
    }
    widgets_templates_krateo_io_LineChart : <<Namespaced>>
    class widgets_templates_krateo_io_NavMenu {
        +string kind: NavMenu
        +string apiVersion: widgets.templates.krateo.io/v1beta1
        +string scope: Namespaced
        +object apiRef
        +string apiRef.name
        +string apiRef.namespace
        +array<object> resourcesRefs
        +array<object> resourcesRefsTemplate
        +object widgetData
        +array<object> widgetData.items
        +array<object> widgetDataTemplate
    }
    widgets_templates_krateo_io_NavMenu : <<Namespaced>>
    class widgets_templates_krateo_io_NavMenuItem {
        +string kind: NavMenuItem
        +string apiVersion: widgets.templates.krateo.io/v1beta1
        +string scope: Namespaced
        +object apiRef
        +string apiRef.name
        +string apiRef.namespace
        +array<object> resourcesRefs
        +array<object> resourcesRefsTemplate
        +object widgetData
        +string widgetData.icon
        +string widgetData.label
        +integer widgetData.order
        +string widgetData.path
        +string widgetData.resourceRefId
        +array<object> widgetDataTemplate
    }
    widgets_templates_krateo_io_NavMenuItem : <<Namespaced>>
    class widgets_templates_krateo_io_Page {
        +string kind: Page
        +string apiVersion: widgets.templates.krateo.io/v1beta1
        +string scope: Namespaced
        +object apiRef
        +string apiRef.name
        +string apiRef.namespace
        +array<object> resourcesRefs
        +array<object> resourcesRefsTemplate
        +object widgetData
        +array<object> widgetData.items
        +string widgetData.title
        +array<object> widgetDataTemplate
    }
    widgets_templates_krateo_io_Page : <<Namespaced>>
    class widgets_templates_krateo_io_Panel {
        +string kind: Panel
        +string apiVersion: widgets.templates.krateo.io/v1beta1
        +string scope: Namespaced
        +object apiRef
        +string apiRef.name
        +string apiRef.namespace
        +array<object> resourcesRefs
        +array<object> resourcesRefsTemplate
        +object widgetData
        +object widgetData.actions
        +string widgetData.clickActionId
        +array<object> widgetData.footer
        +string widgetData.headerLeft
        +string widgetData.headerRight
        +object widgetData.icon
        +array<object> widgetData.items
        +array<string> widgetData.tags
        +string widgetData.title
        +string widgetData.tooltip
        +array<object> widgetDataTemplate
    }
    widgets_templates_krateo_io_Panel : <<Namespaced>>
    class widgets_templates_krateo_io_Paragraph {
        +string kind: Paragraph
        +string apiVersion: widgets.templates.krateo.io/v1beta1
        +string scope: Namespaced
        +object apiRef
        +string apiRef.name
        +string apiRef.namespace
        +array<object> resourcesRefs
        +array<object> resourcesRefsTemplate
        +object widgetData
        +string widgetData.text
        +array<object> widgetDataTemplate
    }
    widgets_templates_krateo_io_Paragraph : <<Namespaced>>
    class widgets_templates_krateo_io_PieChart {
        +string kind: PieChart
        +string apiVersion: widgets.templates.krateo.io/v1beta1
        +string scope: Namespaced
        +object apiRef
        +string apiRef.name
        +string apiRef.namespace
        +array<object> resourcesRefs
        +array<object> resourcesRefsTemplate
        +object widgetData
        +string widgetData.description
        +object widgetData.series
        +string widgetData.title
        +array<object> widgetDataTemplate
    }
    widgets_templates_krateo_io_PieChart : <<Namespaced>>
    class widgets_templates_krateo_io_Route {
        +string kind: Route
        +string apiVersion: widgets.templates.krateo.io/v1beta1
        +string scope: Namespaced
        +object apiRef
        +string apiRef.name
        +string apiRef.namespace
        +array<object> resourcesRefs
        +array<object> resourcesRefsTemplate
        +object widgetData
        +string widgetData.path
        +string widgetData.resourceRefId
        +array<object> widgetDataTemplate
    }
    widgets_templates_krateo_io_Route : <<Namespaced>>
    class widgets_templates_krateo_io_RoutesLoader {
        +string kind: RoutesLoader
        +string apiVersion: widgets.templates.krateo.io/v1beta1
        +string scope: Namespaced
        +object apiRef
        +string apiRef.name
        +string apiRef.namespace
        +array<object> resourcesRefs
        +array<object> resourcesRefsTemplate
        +object widgetData
        +array<object> widgetDataTemplate
    }
    widgets_templates_krateo_io_RoutesLoader : <<Namespaced>>
    class widgets_templates_krateo_io_Row {
        +string kind: Row
        +string apiVersion: widgets.templates.krateo.io/v1beta1
        +string scope: Namespaced
        +object apiRef
        +string apiRef.name
        +string apiRef.namespace
        +array<object> resourcesRefs
        +array<object> resourcesRefsTemplate
        +object widgetData
        +array<object> widgetData.items
        +array<object> widgetDataTemplate
    }
    widgets_templates_krateo_io_Row : <<Namespaced>>
    class widgets_templates_krateo_io_TabList {
        +string kind: TabList
        +string apiVersion: widgets.templates.krateo.io/v1beta1
        +string scope: Namespaced
        +object apiRef
        +string apiRef.name
        +string apiRef.namespace
        +array<object> resourcesRefs
        +array<object> resourcesRefsTemplate
        +object widgetData
        +array<object> widgetData.items
        +array<object> widgetDataTemplate
    }
    widgets_templates_krateo_io_TabList : <<Namespaced>>
    class widgets_templates_krateo_io_Table {
        +string kind: Table
        +string apiVersion: widgets.templates.krateo.io/v1beta1
        +string scope: Namespaced
        +object apiRef
        +string apiRef.name
        +string apiRef.namespace
        +array<object> resourcesRefs
        +array<object> resourcesRefsTemplate
        +object widgetData
        +array<object> widgetData.columns
        +array<object> widgetData.data
        +integer widgetData.pageSize
        +string widgetData.prefix
        +array<object> widgetDataTemplate
    }
    widgets_templates_krateo_io_Table : <<Namespaced>>
    class widgets_templates_krateo_io_YamlViewer {
        +string kind: YamlViewer
        +string apiVersion: widgets.templates.krateo.io/v1beta1
        +string scope: Namespaced
        +object apiRef
        +string apiRef.name
        +string apiRef.namespace
        +array<object> resourcesRefs
        +array<object> resourcesRefsTemplate
        +object widgetData
        +string widgetData.json
        +array<object> widgetDataTemplate
    }
    widgets_templates_krateo_io_YamlViewer : <<Namespaced>>
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Button : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Button : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Button : similar schema
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Column : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Column : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Column : similar schema
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_DataGrid : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_DataGrid : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_DataGrid : similar schema
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_EventList : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_EventList : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_EventList : similar schema
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Filters : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Filters : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Filters : similar schema
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_FlowChart : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_FlowChart : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_FlowChart : similar schema
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Form : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Form : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Form : similar schema
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_LineChart : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_LineChart : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_LineChart : similar schema
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_NavMenuItem : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_NavMenuItem : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_NavMenuItem : similar schema
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_NavMenu : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_NavMenu : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_NavMenu : similar schema
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Page : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Page : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Page : similar schema
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Panel : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Panel : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Panel : similar schema
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Paragraph : similar schema
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_PieChart : similar schema
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Route : similar schema
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_RoutesLoader : similar schema
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Row : similar schema
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_Table : similar schema
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_TabList : similar schema
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_BarChart --> widgets_templates_krateo_io_YamlViewer : similar schema
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Column : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Column : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Column : similar schema
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_DataGrid : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_DataGrid : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_DataGrid : similar schema
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_EventList : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_EventList : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_EventList : similar schema
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Filters : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Filters : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Filters : similar schema
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_FlowChart : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_FlowChart : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_FlowChart : similar schema
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Form : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Form : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Form : similar schema
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_LineChart : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_LineChart : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_LineChart : similar schema
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_NavMenuItem : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_NavMenuItem : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_NavMenuItem : similar schema
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_NavMenu : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_NavMenu : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_NavMenu : similar schema
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Page : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Page : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Page : similar schema
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Panel : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Panel : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Panel : similar schema
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Paragraph : similar schema
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_PieChart : similar schema
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Route : similar schema
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_RoutesLoader : similar schema
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Row : similar schema
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_Table : similar schema
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_TabList : similar schema
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_Button --> widgets_templates_krateo_io_YamlViewer : similar schema
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_DataGrid : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_DataGrid : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_DataGrid : uses
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_DataGrid : similar schema
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_EventList : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_EventList : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_EventList : similar schema
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Filters : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Filters : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Filters : similar schema
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_FlowChart : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_FlowChart : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_FlowChart : similar schema
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Form : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Form : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Form : similar schema
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_LineChart : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_LineChart : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_LineChart : similar schema
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_NavMenuItem : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_NavMenuItem : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_NavMenuItem : similar schema
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_NavMenu : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_NavMenu : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_NavMenu : similar schema
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Page : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Page : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Page : similar schema
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Panel : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Panel : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Panel : similar schema
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Paragraph : similar schema
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_PieChart : similar schema
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Route : similar schema
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_RoutesLoader : similar schema
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Row : similar schema
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Table : uses
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_Table : similar schema
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_TabList : similar schema
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_Column --> widgets_templates_krateo_io_YamlViewer : similar schema
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_EventList : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_EventList : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_EventList : similar schema
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_Filters : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_Filters : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_Filters : similar schema
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_FlowChart : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_FlowChart : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_FlowChart : similar schema
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_Form : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_Form : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_Form : similar schema
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_LineChart : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_LineChart : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_LineChart : similar schema
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_NavMenuItem : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_NavMenuItem : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_NavMenuItem : similar schema
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_NavMenu : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_NavMenu : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_NavMenu : similar schema
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_Page : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_Page : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_Page : similar schema
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_Panel : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_Panel : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_Panel : similar schema
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_Paragraph : similar schema
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_PieChart : similar schema
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_Route : similar schema
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_RoutesLoader : similar schema
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_Row : similar schema
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_Table : similar schema
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_TabList : similar schema
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_DataGrid --> widgets_templates_krateo_io_YamlViewer : similar schema
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Filters : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Filters : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Filters : similar schema
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_FlowChart : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_FlowChart : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_FlowChart : similar schema
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Form : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Form : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Form : uses
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Form : similar schema
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_LineChart : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_LineChart : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_LineChart : similar schema
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_NavMenuItem : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_NavMenuItem : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_NavMenuItem : similar schema
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_NavMenu : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_NavMenu : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_NavMenu : similar schema
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Page : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Page : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Page : similar schema
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Panel : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Panel : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Panel : similar schema
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Paragraph : similar schema
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_PieChart : similar schema
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Route : similar schema
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_RoutesLoader : similar schema
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Row : similar schema
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_Table : similar schema
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_TabList : similar schema
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_EventList --> widgets_templates_krateo_io_YamlViewer : similar schema
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_FlowChart : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_FlowChart : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_FlowChart : similar schema
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_Form : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_Form : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_Form : similar schema
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_LineChart : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_LineChart : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_LineChart : similar schema
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_NavMenuItem : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_NavMenuItem : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_NavMenuItem : similar schema
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_NavMenu : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_NavMenu : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_NavMenu : similar schema
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_Page : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_Page : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_Page : similar schema
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_Panel : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_Panel : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_Panel : similar schema
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_Paragraph : similar schema
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_PieChart : similar schema
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_Route : similar schema
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_RoutesLoader : similar schema
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_Row : similar schema
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_Table : similar schema
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_TabList : similar schema
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_Filters --> widgets_templates_krateo_io_YamlViewer : similar schema
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_Form : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_Form : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_Form : similar schema
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_LineChart : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_LineChart : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_LineChart : similar schema
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_NavMenuItem : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_NavMenuItem : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_NavMenuItem : similar schema
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_NavMenu : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_NavMenu : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_NavMenu : similar schema
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_Page : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_Page : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_Page : similar schema
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_Panel : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_Panel : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_Panel : similar schema
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_Paragraph : similar schema
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_PieChart : similar schema
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_Route : similar schema
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_RoutesLoader : similar schema
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_Row : similar schema
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_Table : similar schema
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_TabList : similar schema
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_FlowChart --> widgets_templates_krateo_io_YamlViewer : similar schema
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_LineChart : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_LineChart : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_LineChart : similar schema
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_NavMenuItem : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_NavMenuItem : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_NavMenuItem : similar schema
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_NavMenu : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_NavMenu : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_NavMenu : similar schema
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_Page : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_Page : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_Page : similar schema
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_Panel : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_Panel : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_Panel : similar schema
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_Paragraph : similar schema
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_PieChart : similar schema
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_Route : similar schema
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_RoutesLoader : similar schema
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_Row : similar schema
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_Table : similar schema
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_TabList : similar schema
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_Form --> widgets_templates_krateo_io_YamlViewer : similar schema
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_NavMenuItem : references
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_NavMenuItem : references
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_NavMenuItem : similar schema
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_NavMenu : references
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_NavMenu : references
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_NavMenu : similar schema
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_Page : references
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_Page : references
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_Page : similar schema
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_Panel : references
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_Panel : references
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_Panel : similar schema
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_Paragraph : similar schema
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_PieChart : similar schema
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_Route : similar schema
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_RoutesLoader : similar schema
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_Row : similar schema
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_Table : similar schema
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_TabList : similar schema
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_LineChart --> widgets_templates_krateo_io_YamlViewer : similar schema
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_NavMenu : references
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_NavMenu : references
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_NavMenu : uses
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_NavMenu : similar schema
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_Page : references
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_Page : references
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_Page : similar schema
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_Panel : references
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_Panel : references
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_Panel : similar schema
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_Paragraph : similar schema
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_PieChart : similar schema
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_Route : similar schema
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_RoutesLoader : similar schema
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_Row : similar schema
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_Table : similar schema
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_TabList : similar schema
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_NavMenuItem --> widgets_templates_krateo_io_YamlViewer : similar schema
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_Page : references
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_Page : references
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_Page : similar schema
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_Panel : references
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_Panel : references
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_Panel : similar schema
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_Paragraph : similar schema
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_PieChart : similar schema
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_Route : similar schema
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_RoutesLoader : similar schema
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_Row : similar schema
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_Table : similar schema
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_TabList : similar schema
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_NavMenu --> widgets_templates_krateo_io_YamlViewer : similar schema
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_Panel : references
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_Panel : references
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_Panel : similar schema
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_Paragraph : similar schema
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_PieChart : similar schema
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_Route : uses
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_Route : similar schema
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_Route : flows to
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_RoutesLoader : similar schema
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_Row : similar schema
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_Table : uses
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_Table : similar schema
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_TabList : similar schema
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_Page --> widgets_templates_krateo_io_YamlViewer : similar schema
    widgets_templates_krateo_io_Panel --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_Panel --> widgets_templates_krateo_io_Paragraph : references
    widgets_templates_krateo_io_Panel --> widgets_templates_krateo_io_Paragraph : similar schema
    widgets_templates_krateo_io_Panel --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_Panel --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_Panel --> widgets_templates_krateo_io_PieChart : similar schema
    widgets_templates_krateo_io_Panel --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_Panel --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_Panel --> widgets_templates_krateo_io_Route : similar schema
    widgets_templates_krateo_io_Panel --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_Panel --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_Panel --> widgets_templates_krateo_io_RoutesLoader : similar schema
    widgets_templates_krateo_io_Panel --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_Panel --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_Panel --> widgets_templates_krateo_io_Row : similar schema
    widgets_templates_krateo_io_Panel --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_Panel --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_Panel --> widgets_templates_krateo_io_Table : similar schema
    widgets_templates_krateo_io_Panel --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_Panel --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_Panel --> widgets_templates_krateo_io_TabList : similar schema
    widgets_templates_krateo_io_Panel --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_Panel --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_Panel --> widgets_templates_krateo_io_YamlViewer : similar schema
    widgets_templates_krateo_io_Paragraph --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_Paragraph --> widgets_templates_krateo_io_PieChart : references
    widgets_templates_krateo_io_Paragraph --> widgets_templates_krateo_io_PieChart : similar schema
    widgets_templates_krateo_io_Paragraph --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_Paragraph --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_Paragraph --> widgets_templates_krateo_io_Route : similar schema
    widgets_templates_krateo_io_Paragraph --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_Paragraph --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_Paragraph --> widgets_templates_krateo_io_RoutesLoader : similar schema
    widgets_templates_krateo_io_Paragraph --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_Paragraph --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_Paragraph --> widgets_templates_krateo_io_Row : similar schema
    widgets_templates_krateo_io_Paragraph --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_Paragraph --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_Paragraph --> widgets_templates_krateo_io_Table : similar schema
    widgets_templates_krateo_io_Paragraph --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_Paragraph --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_Paragraph --> widgets_templates_krateo_io_TabList : similar schema
    widgets_templates_krateo_io_Paragraph --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_Paragraph --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_Paragraph --> widgets_templates_krateo_io_YamlViewer : similar schema
    widgets_templates_krateo_io_PieChart --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_PieChart --> widgets_templates_krateo_io_Route : references
    widgets_templates_krateo_io_PieChart --> widgets_templates_krateo_io_Route : similar schema
    widgets_templates_krateo_io_PieChart --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_PieChart --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_PieChart --> widgets_templates_krateo_io_RoutesLoader : similar schema
    widgets_templates_krateo_io_PieChart --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_PieChart --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_PieChart --> widgets_templates_krateo_io_Row : similar schema
    widgets_templates_krateo_io_PieChart --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_PieChart --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_PieChart --> widgets_templates_krateo_io_Table : similar schema
    widgets_templates_krateo_io_PieChart --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_PieChart --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_PieChart --> widgets_templates_krateo_io_TabList : similar schema
    widgets_templates_krateo_io_PieChart --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_PieChart --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_PieChart --> widgets_templates_krateo_io_YamlViewer : similar schema
    widgets_templates_krateo_io_Route --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_Route --> widgets_templates_krateo_io_RoutesLoader : references
    widgets_templates_krateo_io_Route --> widgets_templates_krateo_io_RoutesLoader : similar schema
    widgets_templates_krateo_io_Route --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_Route --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_Route --> widgets_templates_krateo_io_Row : similar schema
    widgets_templates_krateo_io_Route --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_Route --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_Route --> widgets_templates_krateo_io_Table : similar schema
    widgets_templates_krateo_io_Route --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_Route --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_Route --> widgets_templates_krateo_io_TabList : similar schema
    widgets_templates_krateo_io_Route --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_Route --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_Route --> widgets_templates_krateo_io_YamlViewer : similar schema
    widgets_templates_krateo_io_RoutesLoader --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_RoutesLoader --> widgets_templates_krateo_io_Row : references
    widgets_templates_krateo_io_RoutesLoader --> widgets_templates_krateo_io_Row : similar schema
    widgets_templates_krateo_io_RoutesLoader --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_RoutesLoader --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_RoutesLoader --> widgets_templates_krateo_io_Table : similar schema
    widgets_templates_krateo_io_RoutesLoader --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_RoutesLoader --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_RoutesLoader --> widgets_templates_krateo_io_TabList : similar schema
    widgets_templates_krateo_io_RoutesLoader --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_RoutesLoader --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_RoutesLoader --> widgets_templates_krateo_io_YamlViewer : similar schema
    widgets_templates_krateo_io_Row --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_Row --> widgets_templates_krateo_io_Table : references
    widgets_templates_krateo_io_Row --> widgets_templates_krateo_io_Table : similar schema
    widgets_templates_krateo_io_Row --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_Row --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_Row --> widgets_templates_krateo_io_TabList : similar schema
    widgets_templates_krateo_io_Row --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_Row --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_Row --> widgets_templates_krateo_io_YamlViewer : similar schema
    widgets_templates_krateo_io_Table --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_Table --> widgets_templates_krateo_io_TabList : references
    widgets_templates_krateo_io_Table --> widgets_templates_krateo_io_TabList : similar schema
    widgets_templates_krateo_io_Table --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_Table --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_Table --> widgets_templates_krateo_io_YamlViewer : similar schema
    widgets_templates_krateo_io_TabList --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_TabList --> widgets_templates_krateo_io_YamlViewer : references
    widgets_templates_krateo_io_TabList --> widgets_templates_krateo_io_YamlViewer : similar schema
```
### Detailed CRD Documentation

#### BarChart

**Full Name:** `barcharts.widgets.templates.krateo.io`  
**API Version:** `widgets.templates.krateo.io/v1beta1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** widgets, krateo  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `widgetData` | `object` | ✓ | *No description* |
| `apiRef` | `object` |  | *No description* |
| `resourcesRefs` | `array<object>` |  | *No description* |
| `resourcesRefsTemplate` | `array<object>` |  | *No description* |
| `widgetDataTemplate` | `array<object>` |  | *No description* |


#### Button

**Full Name:** `buttons.widgets.templates.krateo.io`  
**API Version:** `widgets.templates.krateo.io/v1beta1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** widgets, krateo  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `widgetData` | `object` | ✓ | *No description* |
| `apiRef` | `object` |  | *No description* |
| `resourcesRefs` | `array<object>` |  | *No description* |
| `resourcesRefsTemplate` | `array<object>` |  | *No description* |
| `widgetDataTemplate` | `array<object>` |  | *No description* |


#### Column

**Full Name:** `columns.widgets.templates.krateo.io`  
**API Version:** `widgets.templates.krateo.io/v1beta1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** widgets, krateo  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `resourcesRefs` | `array<object>` | ✓ | *No description* |
| `widgetData` | `object` | ✓ | *No description* |
| `apiRef` | `object` |  | *No description* |
| `resourcesRefsTemplate` | `array<object>` |  | *No description* |
| `widgetDataTemplate` | `array<object>` |  | *No description* |


#### DataGrid

**Full Name:** `datagrids.widgets.templates.krateo.io`  
**API Version:** `widgets.templates.krateo.io/v1beta1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** widgets, krateo  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `widgetData` | `object` | ✓ | *No description* |
| `apiRef` | `object` |  | *No description* |
| `resourcesRefs` | `array<object>` |  | *No description* |
| `resourcesRefsTemplate` | `array<object>` |  | *No description* |
| `widgetDataTemplate` | `array<object>` |  | *No description* |


#### EventList

**Full Name:** `eventlists.widgets.templates.krateo.io`  
**API Version:** `widgets.templates.krateo.io/v1beta1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** widgets, krateo  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `widgetData` | `object` | ✓ | *No description* |
| `apiRef` | `object` |  | *No description* |
| `resourcesRefs` | `array<object>` |  | *No description* |
| `resourcesRefsTemplate` | `array<object>` |  | *No description* |
| `widgetDataTemplate` | `array<object>` |  | *No description* |


#### Filters

**Full Name:** `filters.widgets.templates.krateo.io`  
**API Version:** `widgets.templates.krateo.io/v1beta1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** widgets, krateo  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `widgetData` | `object` | ✓ | *No description* |
| `apiRef` | `object` |  | *No description* |
| `resourcesRefs` | `array<object>` |  | *No description* |
| `resourcesRefsTemplate` | `array<object>` |  | *No description* |
| `widgetDataTemplate` | `array<object>` |  | *No description* |


#### FlowChart

**Full Name:** `flowcharts.widgets.templates.krateo.io`  
**API Version:** `widgets.templates.krateo.io/v1beta1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** widgets, krateo  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `widgetData` | `object` | ✓ | *No description* |
| `apiRef` | `object` |  | *No description* |
| `resourcesRefs` | `array<object>` |  | *No description* |
| `resourcesRefsTemplate` | `array<object>` |  | *No description* |
| `widgetDataTemplate` | `array<object>` |  | *No description* |


#### Form

**Full Name:** `forms.widgets.templates.krateo.io`  
**API Version:** `widgets.templates.krateo.io/v1beta1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** widgets, krateo  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `widgetData` | `object` | ✓ | the data that will be passed to the widget on the frontend |
| `apiRef` | `object` |  | *No description* |
| `resourcesRefs` | `array<object>` |  | *No description* |
| `resourcesRefsTemplate` | `array<object>` |  | *No description* |
| `widgetDataTemplate` | `array<object>` |  | *No description* |


#### LineChart

**Full Name:** `linecharts.widgets.templates.krateo.io`  
**API Version:** `widgets.templates.krateo.io/v1beta1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** widgets, krateo  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `widgetData` | `object` | ✓ | data used to render the chart including lines and axis la... |
| `apiRef` | `object` |  | *No description* |
| `resourcesRefs` | `array<object>` |  | *No description* |
| `resourcesRefsTemplate` | `array<object>` |  | *No description* |
| `widgetDataTemplate` | `array<object>` |  | *No description* |


#### NavMenu

**Full Name:** `navmenus.widgets.templates.krateo.io`  
**API Version:** `widgets.templates.krateo.io/v1beta1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** widgets, krateo  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `widgetData` | `object` | ✓ | *No description* |
| `apiRef` | `object` |  | *No description* |
| `resourcesRefs` | `array<object>` |  | *No description* |
| `resourcesRefsTemplate` | `array<object>` |  | *No description* |
| `widgetDataTemplate` | `array<object>` |  | *No description* |


#### NavMenuItem

**Full Name:** `navmenuitems.widgets.templates.krateo.io`  
**API Version:** `widgets.templates.krateo.io/v1beta1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** widgets, krateo  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `widgetData` | `object` | ✓ | *No description* |
| `apiRef` | `object` |  | *No description* |
| `resourcesRefs` | `array<object>` |  | *No description* |
| `resourcesRefsTemplate` | `array<object>` |  | *No description* |
| `widgetDataTemplate` | `array<object>` |  | *No description* |


#### Page

**Full Name:** `pages.widgets.templates.krateo.io`  
**API Version:** `widgets.templates.krateo.io/v1beta1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** widgets, krateo  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `widgetData` | `object` | ✓ | *No description* |
| `apiRef` | `object` |  | *No description* |
| `resourcesRefs` | `array<object>` |  | *No description* |
| `resourcesRefsTemplate` | `array<object>` |  | *No description* |
| `widgetDataTemplate` | `array<object>` |  | *No description* |


#### Panel

**Full Name:** `panels.widgets.templates.krateo.io`  
**API Version:** `widgets.templates.krateo.io/v1beta1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** widgets, krateo  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `resourcesRefs` | `array<object>` | ✓ | *No description* |
| `widgetData` | `object` | ✓ | *No description* |
| `apiRef` | `object` |  | *No description* |
| `resourcesRefsTemplate` | `array<object>` |  | *No description* |
| `widgetDataTemplate` | `array<object>` |  | *No description* |


#### Paragraph

**Full Name:** `paragraphs.widgets.templates.krateo.io`  
**API Version:** `widgets.templates.krateo.io/v1beta1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** widgets, krateo  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `widgetData` | `object` | ✓ | *No description* |
| `apiRef` | `object` |  | *No description* |
| `resourcesRefs` | `array<object>` |  | *No description* |
| `resourcesRefsTemplate` | `array<object>` |  | *No description* |
| `widgetDataTemplate` | `array<object>` |  | *No description* |


#### PieChart

**Full Name:** `piecharts.widgets.templates.krateo.io`  
**API Version:** `widgets.templates.krateo.io/v1beta1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** widgets, krateo  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `widgetData` | `object` | ✓ | *No description* |
| `apiRef` | `object` |  | *No description* |
| `resourcesRefs` | `array<object>` |  | *No description* |
| `resourcesRefsTemplate` | `array<object>` |  | *No description* |
| `widgetDataTemplate` | `array<object>` |  | *No description* |


#### Route

**Full Name:** `routes.widgets.templates.krateo.io`  
**API Version:** `widgets.templates.krateo.io/v1beta1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** widgets, krateo  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `widgetData` | `object` | ✓ | *No description* |
| `apiRef` | `object` |  | *No description* |
| `resourcesRefs` | `array<object>` |  | *No description* |
| `resourcesRefsTemplate` | `array<object>` |  | *No description* |
| `widgetDataTemplate` | `array<object>` |  | *No description* |


#### RoutesLoader

**Full Name:** `routesloaders.widgets.templates.krateo.io`  
**API Version:** `widgets.templates.krateo.io/v1beta1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** widgets, krateo  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `widgetData` | `object` | ✓ | *No description* |
| `apiRef` | `object` |  | *No description* |
| `resourcesRefs` | `array<object>` |  | *No description* |
| `resourcesRefsTemplate` | `array<object>` |  | *No description* |
| `widgetDataTemplate` | `array<object>` |  | *No description* |


#### Row

**Full Name:** `rows.widgets.templates.krateo.io`  
**API Version:** `widgets.templates.krateo.io/v1beta1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** widgets, krateo  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `resourcesRefs` | `array<object>` | ✓ | *No description* |
| `widgetData` | `object` | ✓ | the data that will be passed to the widget on the frontend |
| `apiRef` | `object` |  | *No description* |
| `resourcesRefsTemplate` | `array<object>` |  | *No description* |
| `widgetDataTemplate` | `array<object>` |  | *No description* |


#### TabList

**Full Name:** `tablists.widgets.templates.krateo.io`  
**API Version:** `widgets.templates.krateo.io/v1beta1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** widgets, krateo  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `resourcesRefs` | `array<object>` | ✓ | *No description* |
| `widgetData` | `object` | ✓ | the data that will be passed to the widget on the frontend |
| `apiRef` | `object` |  | *No description* |
| `resourcesRefsTemplate` | `array<object>` |  | *No description* |
| `widgetDataTemplate` | `array<object>` |  | *No description* |


#### Table

**Full Name:** `tables.widgets.templates.krateo.io`  
**API Version:** `widgets.templates.krateo.io/v1beta1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** widgets, krateo  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `widgetData` | `object` | ✓ | *No description* |
| `apiRef` | `object` |  | *No description* |
| `resourcesRefs` | `array<object>` |  | *No description* |
| `resourcesRefsTemplate` | `array<object>` |  | *No description* |
| `widgetDataTemplate` | `array<object>` |  | *No description* |


#### YamlViewer

**Full Name:** `yamlviewers.widgets.templates.krateo.io`  
**API Version:** `widgets.templates.krateo.io/v1beta1`  
**Scope:** Namespaced  
**Instances:** 0  
**Categories:** widgets, krateo  

**Schema Properties:**

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `widgetData` | `object` | ✓ | *No description* |
| `apiRef` | `object` |  | *No description* |
| `resourcesRefs` | `array<object>` |  | *No description* |
| `resourcesRefsTemplate` | `array<object>` |  | *No description* |
| `widgetDataTemplate` | `array<object>` |  | *No description* |




## 📚 Appendices

### CRD Index

Complete alphabetical index of all Custom Resource Definitions:

| CRD Name | Kind | API Group | Scope | Instances |
|----------|------|-----------|-------|-----------|
| `barcharts.widgets.templates.krateo.io` | `BarChart` | `widgets.templates.krateo.io` | Namespaced | 0 |
| `buttons.widgets.templates.krateo.io` | `Button` | `widgets.templates.krateo.io` | Namespaced | 0 |
| `columns.widgets.templates.krateo.io` | `Column` | `widgets.templates.krateo.io` | Namespaced | 0 |
| `datagrids.widgets.templates.krateo.io` | `DataGrid` | `widgets.templates.krateo.io` | Namespaced | 0 |
| `eventlists.widgets.templates.krateo.io` | `EventList` | `widgets.templates.krateo.io` | Namespaced | 0 |
| `filters.widgets.templates.krateo.io` | `Filters` | `widgets.templates.krateo.io` | Namespaced | 0 |
| `flowcharts.widgets.templates.krateo.io` | `FlowChart` | `widgets.templates.krateo.io` | Namespaced | 0 |
| `forms.widgets.templates.krateo.io` | `Form` | `widgets.templates.krateo.io` | Namespaced | 0 |
| `linecharts.widgets.templates.krateo.io` | `LineChart` | `widgets.templates.krateo.io` | Namespaced | 0 |
| `navmenuitems.widgets.templates.krateo.io` | `NavMenuItem` | `widgets.templates.krateo.io` | Namespaced | 0 |
| `navmenus.widgets.templates.krateo.io` | `NavMenu` | `widgets.templates.krateo.io` | Namespaced | 0 |
| `pages.widgets.templates.krateo.io` | `Page` | `widgets.templates.krateo.io` | Namespaced | 0 |
| `panels.widgets.templates.krateo.io` | `Panel` | `widgets.templates.krateo.io` | Namespaced | 0 |
| `paragraphs.widgets.templates.krateo.io` | `Paragraph` | `widgets.templates.krateo.io` | Namespaced | 0 |
| `piecharts.widgets.templates.krateo.io` | `PieChart` | `widgets.templates.krateo.io` | Namespaced | 0 |
| `routes.widgets.templates.krateo.io` | `Route` | `widgets.templates.krateo.io` | Namespaced | 0 |
| `routesloaders.widgets.templates.krateo.io` | `RoutesLoader` | `widgets.templates.krateo.io` | Namespaced | 0 |
| `rows.widgets.templates.krateo.io` | `Row` | `widgets.templates.krateo.io` | Namespaced | 0 |
| `tables.widgets.templates.krateo.io` | `Table` | `widgets.templates.krateo.io` | Namespaced | 0 |
| `tablists.widgets.templates.krateo.io` | `TabList` | `widgets.templates.krateo.io` | Namespaced | 0 |
| `yamlviewers.widgets.templates.krateo.io` | `YamlViewer` | `widgets.templates.krateo.io` | Namespaced | 0 |

### Property Types Summary

Property type usage across all CRDs:

| Type | Usage Count |
|------|-------------|
| `array` | 63 |
| `object` | 42 |

### Relationship Matrix

Schema-based relationships detected between CRDs:

| Source CRD | Target CRD | API Group | Relationship Type |
|------------|------------|-----------|-------------------|
| `BarChart` | `Button` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `Button` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `Button` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `BarChart` | `Column` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `Column` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `Column` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `BarChart` | `DataGrid` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `DataGrid` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `DataGrid` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `BarChart` | `EventList` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `EventList` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `EventList` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `BarChart` | `Filters` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `Filters` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `Filters` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `BarChart` | `FlowChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `FlowChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `FlowChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `BarChart` | `Form` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `Form` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `Form` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `BarChart` | `LineChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `LineChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `LineChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `BarChart` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `BarChart` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `BarChart` | `Page` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `Page` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `Page` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `BarChart` | `Panel` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `Panel` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `Panel` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `BarChart` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `BarChart` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `BarChart` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `Route` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `BarChart` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `BarChart` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `Row` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `BarChart` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `Table` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `BarChart` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `TabList` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `BarChart` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `BarChart` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Button` | `Column` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `Column` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `Column` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Button` | `DataGrid` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `DataGrid` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `DataGrid` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Button` | `EventList` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `EventList` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `EventList` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Button` | `Filters` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `Filters` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `Filters` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Button` | `FlowChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `FlowChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `FlowChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Button` | `Form` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `Form` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `Form` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Button` | `LineChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `LineChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `LineChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Button` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Button` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Button` | `Page` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `Page` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `Page` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Button` | `Panel` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `Panel` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `Panel` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Button` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Button` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Button` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `Route` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Button` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Button` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `Row` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Button` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `Table` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Button` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `TabList` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Button` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `Button` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Column` | `DataGrid` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `DataGrid` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `DataGrid` | `widgets.templates.krateo.io (intra-group)` | uses |
| `Column` | `DataGrid` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Column` | `EventList` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `EventList` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `EventList` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Column` | `Filters` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `Filters` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `Filters` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Column` | `FlowChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `FlowChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `FlowChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Column` | `Form` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `Form` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `Form` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Column` | `LineChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `LineChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `LineChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Column` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Column` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Column` | `Page` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `Page` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `Page` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Column` | `Panel` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `Panel` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `Panel` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Column` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Column` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Column` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `Route` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Column` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Column` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `Row` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Column` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `Table` | `widgets.templates.krateo.io (intra-group)` | uses |
| `Column` | `Table` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Column` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `TabList` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Column` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `Column` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `DataGrid` | `EventList` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `EventList` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `EventList` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `DataGrid` | `Filters` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `Filters` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `Filters` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `DataGrid` | `FlowChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `FlowChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `FlowChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `DataGrid` | `Form` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `Form` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `Form` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `DataGrid` | `LineChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `LineChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `LineChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `DataGrid` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `DataGrid` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `DataGrid` | `Page` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `Page` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `Page` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `DataGrid` | `Panel` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `Panel` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `Panel` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `DataGrid` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `DataGrid` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `DataGrid` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `Route` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `DataGrid` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `DataGrid` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `Row` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `DataGrid` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `Table` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `DataGrid` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `TabList` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `DataGrid` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `DataGrid` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `EventList` | `Filters` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `Filters` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `Filters` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `EventList` | `FlowChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `FlowChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `FlowChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `EventList` | `Form` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `Form` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `Form` | `widgets.templates.krateo.io (intra-group)` | uses |
| `EventList` | `Form` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `EventList` | `LineChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `LineChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `LineChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `EventList` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `EventList` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `EventList` | `Page` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `Page` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `Page` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `EventList` | `Panel` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `Panel` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `Panel` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `EventList` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `EventList` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `EventList` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `Route` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `EventList` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `EventList` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `Row` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `EventList` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `Table` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `EventList` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `TabList` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `EventList` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `EventList` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Filters` | `FlowChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `FlowChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `FlowChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Filters` | `Form` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `Form` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `Form` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Filters` | `LineChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `LineChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `LineChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Filters` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Filters` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Filters` | `Page` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `Page` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `Page` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Filters` | `Panel` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `Panel` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `Panel` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Filters` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Filters` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Filters` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `Route` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Filters` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Filters` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `Row` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Filters` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `Table` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Filters` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `TabList` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Filters` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `Filters` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `FlowChart` | `Form` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `Form` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `Form` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `FlowChart` | `LineChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `LineChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `LineChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `FlowChart` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `FlowChart` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `FlowChart` | `Page` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `Page` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `Page` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `FlowChart` | `Panel` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `Panel` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `Panel` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `FlowChart` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `FlowChart` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `FlowChart` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `Route` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `FlowChart` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `FlowChart` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `Row` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `FlowChart` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `Table` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `FlowChart` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `TabList` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `FlowChart` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `FlowChart` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Form` | `LineChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `LineChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `LineChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Form` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Form` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Form` | `Page` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `Page` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `Page` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Form` | `Panel` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `Panel` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `Panel` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Form` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Form` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Form` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `Route` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Form` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Form` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `Row` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Form` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `Table` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Form` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `TabList` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Form` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `Form` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `LineChart` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | references |
| `LineChart` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | references |
| `LineChart` | `NavMenuItem` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `LineChart` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | references |
| `LineChart` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | references |
| `LineChart` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `LineChart` | `Page` | `widgets.templates.krateo.io (intra-group)` | references |
| `LineChart` | `Page` | `widgets.templates.krateo.io (intra-group)` | references |
| `LineChart` | `Page` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `LineChart` | `Panel` | `widgets.templates.krateo.io (intra-group)` | references |
| `LineChart` | `Panel` | `widgets.templates.krateo.io (intra-group)` | references |
| `LineChart` | `Panel` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `LineChart` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `LineChart` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `LineChart` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `LineChart` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `LineChart` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `LineChart` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `LineChart` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `LineChart` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `LineChart` | `Route` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `LineChart` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `LineChart` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `LineChart` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `LineChart` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `LineChart` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `LineChart` | `Row` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `LineChart` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `LineChart` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `LineChart` | `Table` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `LineChart` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `LineChart` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `LineChart` | `TabList` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `LineChart` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `LineChart` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `LineChart` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `NavMenuItem` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenuItem` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenuItem` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | uses |
| `NavMenuItem` | `NavMenu` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `NavMenuItem` | `Page` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenuItem` | `Page` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenuItem` | `Page` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `NavMenuItem` | `Panel` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenuItem` | `Panel` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenuItem` | `Panel` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `NavMenuItem` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenuItem` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenuItem` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `NavMenuItem` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenuItem` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenuItem` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `NavMenuItem` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenuItem` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenuItem` | `Route` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `NavMenuItem` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenuItem` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenuItem` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `NavMenuItem` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenuItem` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenuItem` | `Row` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `NavMenuItem` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenuItem` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenuItem` | `Table` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `NavMenuItem` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenuItem` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenuItem` | `TabList` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `NavMenuItem` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenuItem` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenuItem` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `NavMenu` | `Page` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenu` | `Page` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenu` | `Page` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `NavMenu` | `Panel` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenu` | `Panel` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenu` | `Panel` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `NavMenu` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenu` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenu` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `NavMenu` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenu` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenu` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `NavMenu` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenu` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenu` | `Route` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `NavMenu` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenu` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenu` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `NavMenu` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenu` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenu` | `Row` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `NavMenu` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenu` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenu` | `Table` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `NavMenu` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenu` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenu` | `TabList` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `NavMenu` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenu` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `NavMenu` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Page` | `Panel` | `widgets.templates.krateo.io (intra-group)` | references |
| `Page` | `Panel` | `widgets.templates.krateo.io (intra-group)` | references |
| `Page` | `Panel` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Page` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `Page` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `Page` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Page` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Page` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Page` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Page` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `Page` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `Page` | `Route` | `widgets.templates.krateo.io (intra-group)` | uses |
| `Page` | `Route` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Page` | `Route` | `widgets.templates.krateo.io (intra-group)` | flows_to |
| `Page` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `Page` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `Page` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Page` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `Page` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `Page` | `Row` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Page` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `Page` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `Page` | `Table` | `widgets.templates.krateo.io (intra-group)` | uses |
| `Page` | `Table` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Page` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `Page` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `Page` | `TabList` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Page` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `Page` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `Page` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Panel` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `Panel` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | references |
| `Panel` | `Paragraph` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Panel` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Panel` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Panel` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Panel` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `Panel` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `Panel` | `Route` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Panel` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `Panel` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `Panel` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Panel` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `Panel` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `Panel` | `Row` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Panel` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `Panel` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `Panel` | `Table` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Panel` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `Panel` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `Panel` | `TabList` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Panel` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `Panel` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `Panel` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Paragraph` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Paragraph` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | references |
| `Paragraph` | `PieChart` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Paragraph` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `Paragraph` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `Paragraph` | `Route` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Paragraph` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `Paragraph` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `Paragraph` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Paragraph` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `Paragraph` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `Paragraph` | `Row` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Paragraph` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `Paragraph` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `Paragraph` | `Table` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Paragraph` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `Paragraph` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `Paragraph` | `TabList` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Paragraph` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `Paragraph` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `Paragraph` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `PieChart` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `PieChart` | `Route` | `widgets.templates.krateo.io (intra-group)` | references |
| `PieChart` | `Route` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `PieChart` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `PieChart` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `PieChart` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `PieChart` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `PieChart` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `PieChart` | `Row` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `PieChart` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `PieChart` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `PieChart` | `Table` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `PieChart` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `PieChart` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `PieChart` | `TabList` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `PieChart` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `PieChart` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `PieChart` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Route` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `Route` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | references |
| `Route` | `RoutesLoader` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Route` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `Route` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `Route` | `Row` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Route` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `Route` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `Route` | `Table` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Route` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `Route` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `Route` | `TabList` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Route` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `Route` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `Route` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `RoutesLoader` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `RoutesLoader` | `Row` | `widgets.templates.krateo.io (intra-group)` | references |
| `RoutesLoader` | `Row` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `RoutesLoader` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `RoutesLoader` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `RoutesLoader` | `Table` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `RoutesLoader` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `RoutesLoader` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `RoutesLoader` | `TabList` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `RoutesLoader` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `RoutesLoader` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `RoutesLoader` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Row` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `Row` | `Table` | `widgets.templates.krateo.io (intra-group)` | references |
| `Row` | `Table` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Row` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `Row` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `Row` | `TabList` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Row` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `Row` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `Row` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Table` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `Table` | `TabList` | `widgets.templates.krateo.io (intra-group)` | references |
| `Table` | `TabList` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `Table` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `Table` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `Table` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | similar_schema |
| `TabList` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `TabList` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | references |
| `TabList` | `YamlViewer` | `widgets.templates.krateo.io (intra-group)` | similar_schema |


---

*Documentation generated by k8s-inventory-cli on 2025-09-07 17:05:17*