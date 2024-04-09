export function camelToSnakeCase(originalString: string) {
    return originalString.replace(/([A-Z])/g, "_$1").toLowerCase();
}

export function snakeToCamelCase(originalString: string) {
    return originalString.toLowerCase().replace(/[-_][a-z]/g, (group) => group.slice(-1).toUpperCase()); 
}