/*
THIS IS A GENERATED/BUNDLED FILE BY ESBUILD
if you want to view the source, please visit the github repository of this plugin
*/

var __create = Object.create;
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __getProtoOf = Object.getPrototypeOf;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toESM = (mod, isNodeMode, target) => (target = mod != null ? __create(__getProtoOf(mod)) : {}, __copyProps(
  // If the importer is in node compatibility mode or this is not an ESM
  // file that has been converted to a CommonJS file using a Babel-
  // compatible transform (i.e. "__esModule" has not been set), then set
  // "default" to the CommonJS "module.exports" for node compatibility.
  isNodeMode || !mod || !mod.__esModule ? __defProp(target, "default", { value: mod, enumerable: true }) : target,
  mod
));
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

// main.ts
var main_exports = {};
__export(main_exports, {
  default: () => AppleBooksPlugin
});
module.exports = __toCommonJS(main_exports);
var import_child_process = require("child_process");
var fs = __toESM(require("fs/promises"));
var path = __toESM(require("path"));
var import_util = require("util");
var import_obsidian = require("obsidian");
var exec = (0, import_util.promisify)(import_child_process.exec);
var APPLE_BOOKS_DATA_FOLDER_ABSOLUTE_PATH = `${process.env.HOME}/Library/Containers/com.apple.iBooksX/Data/Documents/`;
var ANNOTATION_DB_FOLDER_ABSOLUTE_PATH = path.join(
  APPLE_BOOKS_DATA_FOLDER_ABSOLUTE_PATH,
  "AEAnnotation"
);
var BOOKS_DB_FOLDER_ABSOLUTE_PATH = path.join(
  APPLE_BOOKS_DATA_FOLDER_ABSOLUTE_PATH,
  "BKLibrary"
);
var DEFAULT_SETTINGS = {
  highlightsFolder: "Apple Books Highlights",
  syncOnStartup: false
};
var AppleBooksPlugin = class extends import_obsidian.Plugin {
  async onload() {
    await this.loadSettings();
    if (this.settings.syncOnStartup) {
      await this.syncHighlightsSafe();
    }
    this.addSettingTab(new AppleBooksSettingTab(this.app, this));
    this.addCommand({
      id: "obsidian-apple-books-plugin-sync-highlights",
      name: "Sync highlights",
      callback: () => {
        this.syncHighlightsSafe();
      }
    });
    this.addRibbonIcon("book", "Apple Books Sync Highlights", () => {
      this.syncHighlightsSafe();
    });
  }
  onunload() {
  }
  async loadSettings() {
    this.settings = Object.assign(
      {},
      DEFAULT_SETTINGS,
      await this.loadData()
    );
  }
  async saveSettings() {
    await this.saveData(this.settings);
  }
  async syncHighlightsSafe() {
    try {
      this.syncHighlights();
    } catch (e) {
      new import_obsidian.Notice("Error in Apple Books Highlight Sync:", e);
    }
  }
  async syncHighlights() {
    const annotationDBFolderFiles = await fs.readdir(ANNOTATION_DB_FOLDER_ABSOLUTE_PATH).catch(() => []);
    const annotationDBFileName = annotationDBFolderFiles.filter((fileName) => fileName.endsWith(".sqlite")).first();
    if (!annotationDBFileName) {
      new import_obsidian.Notice(
        "Apple Books Annotation Database not found, cannot sync."
      );
      return;
    }
    const annotationDBAbsoluteFileName = path.join(
      ANNOTATION_DB_FOLDER_ABSOLUTE_PATH,
      annotationDBFileName
    );
    const booksDBFolderFiles = await fs.readdir(BOOKS_DB_FOLDER_ABSOLUTE_PATH).catch(() => []);
    const booksDBFileName = booksDBFolderFiles.filter((fileName) => fileName.endsWith(".sqlite")).first();
    if (!booksDBFileName) {
      new import_obsidian.Notice("Apple Books Books Database not found, cannot sync.");
      return;
    }
    const booksDBAbsoluteFileName = path.join(
      BOOKS_DB_FOLDER_ABSOLUTE_PATH,
      booksDBFileName
    );
    const annotationDataSelectQuery = "SELECT ZANNOTATIONASSETID,ZANNOTATIONUUID,ZANNOTATIONSELECTEDTEXT from ZAEANNOTATION where ZANNOTATIONDELETED = 0 AND ZANNOTATIONSELECTEDTEXT NOT NULL;";
    const separatorConfig = '-cmd ".separator ||| @@@"';
    const annotationDBResult = await exec(
      `sqlite3 --readonly ${separatorConfig} ${annotationDBAbsoluteFileName} "${annotationDataSelectQuery}"`
    );
    const annotationDBRawRows = annotationDBResult.stdout.split("@@@").filter((a) => !!a);
    const annotationData = annotationDBRawRows.map((row) => row.split("|||")).reduce((acc, row) => {
      if (!acc[row[0]]) {
        acc[row[0]] = [];
      }
      acc[row[0]].push({
        annotationId: row[1],
        selectedText: row[2]
      });
      return acc;
    }, {});
    const uniqueBookIds = Object.keys(annotationData).map((a) => `'${a}'`);
    const booksDataSelectQuery = `SELECT ZASSETID,ZAUTHOR,ZTITLE from ZBKLIBRARYASSET where ZASSETID in (${uniqueBookIds.join(
      ","
    )})`;
    const booksDBResult = await exec(
      `sqlite3 --readonly ${separatorConfig} ${booksDBAbsoluteFileName} "${booksDataSelectQuery}"`
    );
    const booksDBRawRows = booksDBResult.stdout.split("@@@").filter((a) => !!a);
    const booksData = booksDBRawRows.map((row) => row.split("|||"));
    const finalData = {};
    for (const bookData of booksData) {
      const bookId = bookData[0];
      if (!annotationData[bookId]) {
        continue;
      }
      finalData[bookId] = {
        bookId,
        authorName: bookData[1],
        bookTitle: bookData[2],
        highlights: annotationData[bookId]
      };
    }
    const highlightsFolderAbstractFile = this.app.vault.getAbstractFileByPath(
      this.settings.highlightsFolder
    );
    if (highlightsFolderAbstractFile) {
      await this.app.vault.delete(highlightsFolderAbstractFile, true);
    }
    await this.app.vault.createFolder(this.settings.highlightsFolder);
    for (const [, book] of Object.entries(finalData)) {
      const highlightsFolderPath = this.settings.highlightsFolder;
      const fileName = `${book.bookTitle}.md`.replace("\\", " ").replace("/", " ").replace(":", " ");
      const filePath = (0, import_obsidian.normalizePath)(
        path.join(highlightsFolderPath, fileName)
      );
      await this.app.vault.create(
        filePath,
        `## Metadata
- Author: ${book.authorName}
- [Apple Books Link](ibooks://assetid/${book.bookId})

## Highlights
${book.highlights.map((highlight) => highlight.selectedText).join("\n\n---\n")}`
      );
    }
    new import_obsidian.Notice("Successfully finished Apple Books Highlight Sync");
  }
};
var AppleBooksSettingTab = class extends import_obsidian.PluginSettingTab {
  constructor(app, plugin) {
    super(app, plugin);
    this.plugin = plugin;
  }
  display() {
    this.containerEl.empty();
    this.containerEl.createEl("h2", {
      text: "Settings for Apple Books Highlights"
    });
    new import_obsidian.Setting(this.containerEl).setName("Highlights folder location").setDesc(
      "Vault folder to use for saving book highlight notes. Default directory is 'Apple Books Highlights'. WARNING: this folder and all its contents will be deleted on every sync! Use a dedicated folder for this plugin, and do not edit the notes it creates."
    ).addDropdown((dropdown) => {
      const files = this.app.vault.getAllLoadedFiles();
      const folders = files.filter((file) => file instanceof import_obsidian.TFolder);
      folders.map((folder) => folder.path).sort().forEach((path2) => {
        dropdown.addOption(path2, path2);
      });
      return dropdown.setValue(this.plugin.settings.highlightsFolder).onChange(async (value) => {
        this.plugin.settings.highlightsFolder = value;
        await this.plugin.saveSettings();
      });
    });
    new import_obsidian.Setting(this.containerEl).setName("Sync highlights on startup").setDesc(
      "Automatically sync Apple Books highlights when Obsidian starts"
    ).addToggle((toggle) => {
      toggle.setValue(this.plugin.settings.syncOnStartup).onChange(async (value) => {
        this.plugin.settings.syncOnStartup = value;
        await this.plugin.saveSettings();
      });
    });
  }
};

/* nosourcemap */